import requests
from typing import Dict, Any, Optional

class Node:
    def __init__(self, api_key, network="mainnet"):
        self.network = network
        self.base_url = f"https://kaia-{network if network == 'mainnet' else 'kairos'}.nodit.io"
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-KEY": api_key
        }
        self.json_rpc_version = "2.0"

    def _make_request(self, method: str, params: Optional[list] = None) -> Dict[str, Any]:
        payload = {
            "jsonrpc": self.json_rpc_version,
            "id": 1,
            "method": method
        }
        if params is not None:
            payload["params"] = params

        response = requests.post(
            self.base_url,
            headers=self.headers,
            json=payload
        )
        response.raise_for_status()
        return response.json()

    def get_chain_id(self) -> Dict[str, Any]:
        return self._make_request("kaia_chainID")

    def get_block_number(self) -> Dict[str, Any]:
        return self._make_request("kaia_blockNumber")

    def get_balance(self, address: str, block: str = "latest") -> Dict[str, Any]:
        return self._make_request("kaia_getBalance", [address, block])

    def call(
        self,
        transaction: Dict[str, str],
        block: str = "latest",
        state_override: Optional[Dict] = None
    ) -> Dict[str, Any]:
        params = [transaction, block]
        if state_override is not None:
            params.append(state_override)
        return self._make_request("kaia_call", params)

    def create_access_list(
        self,
        transaction: Dict[str, str],
        block: str = "latest"
    ) -> Dict[str, Any]:
        return self._make_request("kaia_createAccessList", [transaction, block])

    def estimate_gas(self, transaction: Dict[str, str]) -> Dict[str]:
        return self._make_request("kaia_estimateGas", [transaction])

    def get_fee_history(
        self,
        block_count: int,
        newest_block: str = "latest",
        reward_percentiles: Optional[list[float]] = None
    ) -> Dict[str, Any]:
        params = [hex(block_count) if isinstance(block_count, int) else block_count, newest_block]
        if reward_percentiles is not None:
            params.append(reward_percentiles)
        return self._make_request("kaia_feeHistory", params)

    def get_gas_price(self) -> Dict[str, Any]:
        return self._make_request("kaia_gasPrice")

    def get_block_by_hash(self, block_hash: str, include_transactions: bool = True) -> Dict[str, Any]:
        return self._make_request("kaia_getBlockByHash", [block_hash, include_transactions])

    def get_block_by_number(self, block: str, include_transactions: bool = True) -> Dict[str, Any]:
        return self._make_request("kaia_getBlockByNumber", [block, include_transactions])

    def get_block_receipts(self, block: str) -> Dict[str, Any]:
        return self._make_request("kaia_getBlockReceipts", [block])

    def get_transaction_by_hash(self, transaction_hash: str) -> Dict[str, Any]:
        return self._make_request("kaia_getTransactionByHash", [transaction_hash])  
    
    def get_transaction_by_block_hash_and_index(self, block_hash: str, index: int) -> Dict[str, Any]:
        return self._make_request("kaia_getTransactionByBlockHashAndIndex", [block_hash, index])

    def get_transaction_by_block_number_and_index(self, block: str, index: int) -> Dict[str, Any]:  
        return self._make_request("kaia_getTransactionByBlockNumberAndIndex", [block, index])   
    
    def get_transaction_receipt(self, transaction_hash: str) -> Dict[str, Any]:
        return self._make_request("kaia_getTransactionReceipt", [transaction_hash]) 
    
    def get_transaction_count(self, address: str, block: str = "latest") -> Dict[str, Any]:
        return self._make_request("kaia_getTransactionCount", [address, block])        

    def get_storage_at(self, address: str, position: str, block: str = "latest") -> Dict[str, Any]:
        return self._make_request("kaia_getStorageAt", [address, position, block])      
    
    def get_code(self, address: str, block: str = "latest") -> Dict[str, Any]:
        return self._make_request("kaia_getCode", [address, block])
    
    def get_block_transaction_count_by_hash(self, block_hash: str) -> Dict[str, Any]:
        return self._make_request("kaia_getBlockTransactionCountByHash", [block_hash])

    def get_block_transaction_count_by_number(self, block: str) -> Dict[str, Any]:
        return self._make_request("kaia_getBlockTransactionCountByNumber", [block])

    def get_filter_changes(self, filter_id: str) -> Dict[str, Any]:
        return self._make_request("kaia_getFilterChanges", [filter_id])

    def get_filter_logs(self, filter_id: str) -> Dict[str, Any]:
        return self._make_request("kaia_getFilterLogs", [filter_id])

    def get_logs(self, filter_obj: Dict[str, Any]) -> Dict[str, Any]:
        return self._make_request("kaia_getLogs", [filter_obj])

    def get_proof(self, address: str, storage_hashes: list[str], block: str = "latest") -> Dict[str, Any]:
        return self._make_request("kaia_getProof", [address, storage_hashes, block])

    def get_max_priority_fee_per_gas(self) -> Dict[str, Any]:
        return self._make_request("kaia_maxPriorityFeePerGas")

    def new_block_filter(self) -> Dict[str, Any]:
        return self._make_request("kaia_newBlockFilter")

    def new_filter(self, filter_obj: Dict[str, Any]) -> Dict[str, Any]:
        return self._make_request("kaia_newFilter", [filter_obj])

    def new_pending_transaction_filter(self) -> Dict[str, Any]:
        return self._make_request("kaia_newPendingTransactionFilter")

    def send_raw_transaction(self, signed_transaction_hash: str) -> Dict[str, Any]:
        return self._make_request("kaia_sendRawTransaction", [signed_transaction_hash])

    def uninstall_filter(self, filter_id: str) -> Dict[str, Any]:
        return self._make_request("kaia_uninstallFilter", [filter_id])
