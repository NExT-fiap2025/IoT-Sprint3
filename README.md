# 🧑‍💻 Sistema de Reconhecimento Facial com Dlib e OpenCV

## 📌 Integrantes

-Eduardo Gomes Pinho Junior - 97919
-Gustavo Ferreira Lopes - 98887
-Pedro Henrique Salvitti - 88166
-Enzo de Oliveira Cunha - 550985

## 📌 Objetivo

Este projeto implementa um **sistema de reconhecimento facial**
utilizando **OpenCV** e **Dlib**, sem dependência de hardware externo
(como Arduino).\
Ele permite:\
- Cadastrar novos usuários.\
- Validar rostos em tempo real via webcam.\
- Listar usuários cadastrados.\
- Excluir usuários do banco local.

O banco de usuários é armazenado em um arquivo local (`db.pkl`).

------------------------------------------------------------------------

## ⚙️ Dependências

Antes de rodar o projeto, instale as bibliotecas necessárias
(recomenda-se usar **ambiente virtual**):

``` bash
pip install opencv-python dlib numpy
```

------------------------------------------------------------------------

## 🔹 Modelos necessários

O projeto utiliza modelos pré-treinados do **dlib**, que não estão
incluídos no repositório devido ao tamanho.\
Você precisa baixar manualmente e colocar os arquivos na **pasta raiz do
projeto**.

-   [shape_predictor_5\_face_landmarks.dat.bz2](http://dlib.net/files/shape_predictor_5_face_landmarks.dat.bz2)\
-   [dlib_face_recognition_resnet_model_v1.dat.bz2](http://dlib.net/files/dlib_face_recognition_resnet_model_v1.dat.bz2)\
-   [shape_predictor_68_face_landmarks.dat.bz2](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)

Após o download, descompacte os arquivos:

``` bash
bzip2 -d nome_do_arquivo.bz2
```

------------------------------------------------------------------------

## ▶️ Execução

Para rodar o projeto:

``` bash
python ReconTest.py
```

O sistema abrirá a webcam e mostrará as opções no terminal:

-   **\[C\]** → Cadastrar novo rosto\
-   **\[V\]** → Ativar/desativar validação de rostos\
-   **\[L\]** → Listar usuários cadastrados\
-   **\[X\]** → Excluir usuário\
-   **\[S\]** → Sair

------------------------------------------------------------------------

## 🗂️ Estrutura do projeto

    📂 Projeto
     ┣ 📜 main.py              # Código principal
     ┣ 📜 db.pkl               # Banco de embeddings faciais (gerado automaticamente)
     ┣ 📜 shape_predictor_5_face_landmarks.dat
     ┣ 📜 shape_predictor_68_face_landmarks.dat
     ┣ 📜 dlib_face_recognition_resnet_model_v1.dat
     ┗ 📜 README.md

------------------------------------------------------------------------

## ⚡ Parâmetros importantes

-   **THRESH = 0.6**\
    Define a tolerância de similaridade entre rostos. Valores menores
    deixam o sistema mais rigoroso, valores maiores tornam mais
    permissivo.

------------------------------------------------------------------------

## ⚖️ Nota ética sobre uso de dados faciais

Este projeto foi desenvolvido **exclusivamente para fins educacionais e
de pesquisa**.\
- O uso de reconhecimento facial envolve **dados biométricos
sensíveis**.\
- Nunca utilize este código em ambientes de produção sem consentimento
explícito das pessoas envolvidas.\
- O armazenamento e processamento de rostos deve seguir legislações
locais (LGPD, GDPR etc.).
