from typing import Optional, List, Dict, Any
from .client import Client

class Statistics:
    def __init__(self, api_key, network="mainnet"):
        self.client = Client(api_key)
        self.network = network
        self.base_path = f"/v1/kaia/{network if network == 'mainnet' else 'kairos'}"

    def get_account_stats(
        self,
        address: str
    ) -> Dict[str, Any]:
        endpoint = f"{self.base_path}/stats/getAccountStats"
        payload = {"address": address}
        return self.client.post(endpoint, payload)