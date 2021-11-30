from fastapi import FastAPI

#instancia
app = FastAPI(title="Movies", description="API para calificar películas", version="1")

@app.get("/")
def index():
    return "Movies API"

