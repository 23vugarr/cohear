from pydantic import BaseModel

class UserLogin(BaseModel):
    ...
    
class UserRegister(BaseModel):
    name: str
    surname: str
    phoneNumber: int
    birthday: str
    password: str

