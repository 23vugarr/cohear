from .schemas.user import ProfileInfo
import requests
import streamlit as st
import json

class ProfileController:
    def __init__(self, backend_url: str):
        self._backend_url = backend_url
    
    def get_profile_info(self, phoneNumber):
        response = requests.post(
            f"{self._backend_url}/api/v1/profile",
            json={"phoneNumber": int(phoneNumber)},
            headers={"Authorization": st.session_state.get('jwt')}
        )
    
        print("phonenumber", type(phoneNumber))
        print("jwt", st.session_state.get("jwt"))

        print("Raw response content:", response.content)
    
        try:
            response_json = response.json()
            print("here", response_json)
        except ValueError:
            print("Failed to parse response as JSON")
            return None

        if response.status_code == 200:
            profile_info = ProfileInfo(**response_json['payload'])
            return profile_info
        else:
            print("Error response:", response_json)
            return None