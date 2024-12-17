from typing import Optional, List, Dict, Any
from .client import Client

class Statistics:
    def __init__(self, api_key):
        self.client = Client(api_key)

    def get_account_stats(
        self,
        address: str
    ) -> Dict[str, Any]:
        endpoint = "/v1/kaia/mainnet/stats/getAccountStats"
        payload = {"address": address}
        return self.client.post(endpoint, payload)