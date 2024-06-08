from pydantic import BaseModel

class UserLogin(BaseModel):
    phoneNumber: int
    password: str
    
class UserRegister(BaseModel):
    name: str
    surname: str
    phoneNumber: int
    birthday: str
    password: str
    


