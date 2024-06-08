import requests
from .schemas.user import UserRegister, UserLogin

class AuthController:
    def __init__(self, backend_url: str):
        self._backend_url = backend_url
        pass
    
    def login(self, data: UserLogin) -> bool:
        data.phoneNumber = int(data.phoneNumber)
        data_dict = data.model_dump()

        response = requests.post(f"{self._backend_url}/api/v1/login", json=data_dict)
        print(response.json())
        if response.status_code == 200:
            return True
        else:
            return False

        
    def register(self, data: UserRegister) -> bool:
        data.phoneNumber = int(data.phoneNumber)
        data_dict = data.model_dump()

        response = requests.post(f"{self._backend_url}/api/v1/register", json=data_dict)
        print(response.json())
        if response.status_code == 200:
            return True
        else:
            return False
