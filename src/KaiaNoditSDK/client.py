# client.py

import requests

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