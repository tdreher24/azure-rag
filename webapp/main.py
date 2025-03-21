from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import RedirectResponse

app = FastAPI()

# Simpler Pydantic-Body für POST
class Body(BaseModel):
    query: str

@app.get("/")
def root():
    return {"message": "Hello from Azure Container App 🎉"}

@app.get("/docs-redirect")
def docs_redirect():
    return RedirectResponse(url="/docs")

@app.post("/ask")
def ask(body: Body):
    query = body.query
    response = fake_assistant(query)
    return {"response": response}

def fake_assistant(query: str) -> str:
    """
    Simulierter Antwortgenerator.
    """
    # Du kannst das natürlich fancy machen – aber hier einfach:
    return f"Ich habe deine Frage erhalten: '{query}'. Bald bekommst du eine echte KI-Antwort! 😉"
