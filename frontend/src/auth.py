import requests
from .schemas.user import UserRegister
import json

class AuthController:
    def __init__(self, backend_url: str):
        self._backend_url = backend_url
        pass
    
    def login():
        ...
        
    def register(self, data: UserRegister) -> bool:
        data = data.model_dump_json()
        print(data)
        response = requests.post(f"{self._backend_url}/api/v1/register", json=data)
        print(response.json())
        if response.status_code == 200:
            return True
        else:
            return False