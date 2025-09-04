 Link da API Online

A API está publicada no Render e pode ser acessada através dos seguintes links:

(Health Check)
    [https://minha-api-simples-render.onrender.com/health](https://minha-api-simples-render.onrender.com/health)

Informações Pessoais
    [https://minha-api-simples-render.onrender.com/me](https://minha-api-simples-render.onrender.com/me)

---

Passos (pra eu lembrar depois também):

1. Clone o repositório:
    ```bash
    git clone [https://github.com/ChelyDev/api-simples-render.git](https://github.com/ChelyDev/api-simples-render.git)
    cd api-simples-render
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate

3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4.  Execute o servidor de desenvolvimento:
    ```bash
    uvicorn main:app --reload
    ```

5.  Abra seu navegador e acesse `http://127.0.0.1:8000/`. Os endpoints `/health` e `/me` estarão disponíveis.

---
Endpoints da API

`GET /health`: Endpoint de verificação de status. Retorna `{"status": "ok"}`.
`GET /me`: Retorna informações pessoais da desenvolvedora.