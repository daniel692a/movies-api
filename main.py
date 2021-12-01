from fastapi import FastAPI, HTTPException
from database import database as connection
from database import User, Movie, UserReview
from schemas import UserBM
#instancia
app = FastAPI(title="Movies", description="API para calificar películas", version="1")


# Eventos
@app.on_event("startup")
def startup():
    if connection.is_closed():
        connection.connect()
        print('Connection successful')
    connection.create_tables(models=[User, Movie, UserReview], safe=True)
    print('Server on')

@app.on_event("shutdown")
def shutdown():
    if not connection.is_closed():
        connection.close()
        print('Connection closed')
    print('Server off')


@app.get("/")
async def index():
    return "Movies API"


@app.post('/users')
async def create_user(user: UserBM):

    if User.select().where(User.username == user.username).exists():
        return HTTPException(status_code=409, detail="User already exists")

    hash_password = User.hash_password(user.password)
    user = User.create(username=user.username, password=hash_password)
    return user.id

