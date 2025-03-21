from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from Azure Container App 🎉"}

@app.get("/docs-redirect")
def docs_redirect():
    return RedirectResponse(url="/docs", status_code=301)
