from fastapi import FastAPI
from database import database as connection

#instancia
app = FastAPI(title="Movies", description="API para calificar películas", version="1")


# Eventos
@app.on_event("startup")
def startup():
    if connection.is_closed():
        connection.connect()
        print('Connection successful')
    print('Server on')

@app.on_event("shutdown")
def shutdown():
    if not connection.is_closed():
        connection.close()
    print('Server off')


@app.get("/")
async def index():
    return "Movies API"

@app.get('/about')
async def about():
    return "about"

