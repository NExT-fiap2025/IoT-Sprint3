import cv2, dlib, numpy as np, pickle, os, time

# Modelos necessários (precisam estar na pasta do projeto)
PREDICTOR = "shape_predictor_5_face_landmarks.dat"
RECOG = "dlib_face_recognition_resnet_model_v1.dat"
DB_FILE = "db.pkl"
THRESH = 0.6  # Limite de similaridade

# Carrega banco de dados local
db = pickle.load(open(DB_FILE, "rb")) if os.path.exists(DB_FILE) else {}

# Inicializa detector e modelos
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(PREDICTOR)
rec = dlib.face_recognition_model_v1(RECOG)

# Captura da webcam
cap = cv2.VideoCapture(0)
validando = False

print("[C]=Cadastrar  [V]=Validar ON/OFF  [L]=Listar cadastrados  [X]=Excluir usuário  [S]=Sair")

while True:
    ok, frame = cap.read()
    if not ok:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rects = detector(rgb, 1)

    for r in rects:
        # Extrai landmarks e gera embedding facial
        shape = sp(rgb, r)
        chip = dlib.get_face_chip(rgb, shape)
        vec = np.array(rec.compute_face_descriptor(chip), dtype=np.float32)

        # --- Validação ---
        if validando and db:
            nome, dist = "Desconhecido", 999
            for n, v in db.items():
                d = np.linalg.norm(vec - v)
                if d < dist:
                    nome, dist = n, d
            if dist > THRESH:
                nome = "Desconhecido"

            # Caixa e texto
            color = (0, 255, 0) if nome != "Desconhecido" else (0, 0, 255)
            cv2.rectangle(frame, (r.left(), r.top()), (r.right(), r.bottom()), color, 2)
            cv2.putText(frame, nome, (r.left(), r.top()-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # Mostrar status do modo na tela
    status = "ON" if validando else "OFF"
    cv2.putText(frame, status, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

    cv2.imshow("Reconhecimento Facial", frame)
    k = cv2.waitKey(1) & 0xFF

    # [S] = sair
    if k == ord('s'):
        break

    # [V] = alternar modo de validação
    if k == ord('v'):
        validando = not validando
        print("Validação:", "ON" if validando else "OFF")

    # [C] = cadastrar novo rosto
    if k == ord('c') and len(rects) == 1:
        nome = input("Nome: ").strip()
        if nome:
            if nome in db:
                print(f"{nome} já existe no banco! Use outro nome.")
            else:
                db[nome] = vec
                pickle.dump(db, open(DB_FILE, "wb"))
                print("Salvo:", nome)

    # [L] = listar cadastrados
    if k == ord('l'):
        print("Usuários cadastrados:", list(db.keys()) if db else "Nenhum usuário cadastrado.")

    # [X] = excluir usuário
    if k == ord('x'):
        if not db:
            print("Nenhum usuário cadastrado para excluir.")
        else:
            print("Usuários cadastrados:", list(db.keys()))
            nome = input("Digite o nome do usuário para excluir: ").strip()
            if nome in db:
                del db[nome]
                pickle.dump(db, open(DB_FILE, "wb"))
                print(f"Usuário {nome} removido com sucesso.")
            else:
                print(f"Usuário {nome} não encontrado no banco.")

cap.release()
cv2.destroyAllWindows()
