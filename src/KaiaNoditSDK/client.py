import requests
from typing import Optional

class Client:
    def __init__(self, api_key):
        self.base_url = "https://web3.nodit.io"
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-KEY": api_key
        }

    def post(self, endpoint, json_data):
        response = requests.post(f"{self.base_url}{endpoint}", headers=self.headers, json=json_data)
        response.raise_for_status()
        return response.json()
    
    def get(self, endpoint, params=None):
        response = requests.get(f"{self.base_url}{endpoint}", headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
    
    def patch(self, endpoint: str, json_data: dict) -> dict:
        response = requests.patch(
            f"{self.base_url}{endpoint}", 
            headers=self.headers, 
            json=json_data
        )
        response.raise_for_status()
        return response.json()
    
    def delete(self, endpoint: str) -> dict:
        response = requests.delete(
            f"{self.base_url}{endpoint}", 
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()
    
