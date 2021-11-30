from fastapi import FastAPI

#instancia
app = FastAPI(title="Movies", description="API para calificar películas", version="1")


# Eventos
@app.on_event("startup")
def startup():
    print('Server on')

@app.on_event("shutdown")
def shutdown():
    print('Server off')


@app.get("/")
async def index():
    return "Movies API"

@app.get('/about')
async def about():
    return "about"

