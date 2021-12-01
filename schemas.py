from pydantic import BaseModel, validator

class UserRequestModel(BaseModel):
    username: str
    password: str

    @validator('username')
    def username_validation(cls, username):
        if len(username) < 3:
            raise ValueError("Username must be at least 3 characters long")
        elif len(username) > 50:
            raise ValueError("Username must be at most 20 characters long")
        return username

    @validator('password')
    def password_validation(cls, password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if len(password) > 50:
            raise ValueError("Password must be at most 50 characters long")
        return password

class UserResponseModel(BaseModel):
    id: int
    username: str
