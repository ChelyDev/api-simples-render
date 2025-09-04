from fastapi import FastAPI

app = FastAPI()

#main.py

from fastapi import FastAPI

#cria uma instância da aplicação FastAPI
app = FastAPI()

#endpoint 1: /health
@app.get("/health")
def health_check():
    """
    endpoint que retorna um status de ok para indicar que a API está funcionando.
    """
    return {"status": "ok"}

#endpoint 2: /me
@app.get("/me")
def get_personal_info():
    """
    endpoint que retorna informações pessoais.
    """

    aluno_info = {
        "nome": "Michely Costa Dantas",
        "email": "37023403@sempreunijuazeiro.com.br",
        "curso": "Sistemas de Informação",
        "github": "https://github.com/ChelyDev",
        "cidade": "Porteiras/CE",
        "interesses": ["Concurso Público", "SI", "Dormir"] 
    }
    return aluno_info