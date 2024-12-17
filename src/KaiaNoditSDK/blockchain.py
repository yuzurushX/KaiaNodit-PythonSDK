from typing import Optional, List, Dict, Any
from .client import Client

class Blockchain:
    def __init__(self, api_key):
        self.client = Client(api_key)

    def get_block_by_hash_or_number(
        self,
        block: str
    ) -> Dict[str, Any]:
        endpoint = "/v1/kaia/mainnet/blockchain/getBlockByHashOrNumber"
        payload = {"block": block}
        return self.client.post(endpoint, payload)

    def get_blocks_within_range(
        self,
        from_block: Optional[str] = None,
        to_block: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        page: Optional[int] = None,
        rpp: int = 10,
        cursor: Optional[str] = None,
        with_count: Optional[bool] = None
    ) -> Dict[str, Any]:
        endpoint = "/v1/kaia/mainnet/blockchain/getBlocksWithinRange"
        payload = {}
        
        if from_block is not None:
            payload["fromBlock"] = from_block
        if to_block is not None:
            payload["toBlock"] = to_block
        if from_date is not None:
            payload["fromDate"] = from_date
        if to_date is not None:
            payload["toDate"] = to_date
        if page is not None:
            payload["page"] = page
        if rpp is not None:
            payload["rpp"] = rpp
        if cursor is not None:
            payload["cursor"] = cursor
        if with_count is not None:
            payload["withCount"] = with_count
        
        return self.client.post(endpoint, payload)

    def get_gas_price(self) -> Dict[str, Any]:
        endpoint = "/v1/kaia/mainnet/blockchain/getGasPrice"
        payload = {}
        return self.client.post(endpoint, payload)
    
    def get_internal_transactions_by_account(
        self,
        account_address: str,
        page: Optional[int] = None,
        rpp: int = 10,
        cursor: Optional[str] = None,
        with_count: Optional[bool] = None,
        with_zero_value: Optional[bool] = None,
        with_external_transaction: Optional[bool] = None
    ) -> Dict[str, Any]:
        endpoint = "/v1/kaia/mainnet/blockchain/getInternalTransactionsByAccount"
        payload = {"accountAddress": account_address}
        
        if page is not None:
            payload["page"] = page
        if rpp is not None:
            payload["rpp"] = rpp
        if cursor is not None:
            payload["cursor"] = cursor
        if with_count is not None:
            payload["withCount"] = with_count
        if with_zero_value is not None:
            payload["withZeroValue"] = with_zero_value
        if with_external_transaction is not None:
            payload["withExternalTransaction"] = with_external_transaction
        
        return self.client.post(endpoint, payload)


    def get_next_nonce_by_account(
        self,
        account_address: str
    ) -> Dict[str, Any]:
        endpoint = "/v1/kaia/mainnet/blockchain/getNextNonceByAccount"
        payload = {"accountAddress": account_address}
        return self.client.post(endpoint, payload)

    def get_transaction_by_hash(
        self,
        transaction_hash: str,
        with_logs: Optional[bool] = None,
        with_decode: Optional[bool] = None
    ) -> Dict[str, Any]:
        endpoint = "/v1/kaia/mainnet/blockchain/getTransactionByHash"
        payload = {"transactionHash": transaction_hash}
        
        if with_logs is not None:
            payload["withLogs"] = with_logs
        if with_decode is not None:
            payload["withDecode"] = with_decode
        
        return self.client.post(endpoint, payload)

    def get_transactions_by_account(
        self,
        account_address: str,
        relation: Optional[str] = None,
        from_block: Optional[str] = None,
        to_block: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        page: Optional[int] = None,
        rpp: int = 10,
        cursor: Optional[str] = None,
        with_count: Optional[bool] = None,
        with_logs: Optional[bool] = None,
        with_decode: Optional[bool] = None
    ) -> Dict[str, Any]:
        endpoint = "/v1/kaia/mainnet/blockchain/getTransactionsByAccount"
        payload = {"accountAddress": account_address}
        
        if relation is not None:
            payload["relation"] = relation
        if from_block is not None:
            payload["fromBlock"] = from_block
        if to_block is not None:
            payload["toBlock"] = to_block
        if from_date is not None:
            payload["fromDate"] = from_date
        if to_date is not None:
            payload["toDate"] = to_date
        if page is not None:
            payload["page"] = page
        if rpp is not None:
            payload["rpp"] = rpp
        if cursor is not None:
            payload["cursor"] = cursor
        if with_count is not None:
            payload["withCount"] = with_count
        if with_logs is not None:
            payload["withLogs"] = with_logs
        if with_decode is not None:
            payload["withDecode"] = with_decode
        
        return self.client.post(endpoint, payload)

    def get_transactions_by_hashes(
        self,
        transaction_hashes: List[str],
        with_logs: Optional[bool] = None,
        with_decode: Optional[bool] = None
    ) -> Dict[str, Any]:
        endpoint = "/v1/kaia/mainnet/blockchain/getTransactionsByHashes"
        payload = {"transactionHashes": transaction_hashes}
        
        if with_logs is not None:
            payload["withLogs"] = with_logs
        if with_decode is not None:
            payload["withDecode"] = with_decode
        
        return self.client.post(endpoint, payload)

    def get_transactions_in_block(
        self,
        block: str,
        page: Optional[int] = None,
        rpp: Optional[int] = None,
        cursor: Optional[str] = None,
        with_count: Optional[bool] = None,
        with_logs: Optional[bool] = None,
        with_decode: Optional[bool] = None
    ) -> Dict[str, Any]:
        endpoint = "/v1/kaia/mainnet/blockchain/getTransactionsInBlock"
        payload = {"block": block}
        
        if page is not None:
            payload["page"] = page
        if rpp is not None:
            payload["rpp"] = rpp
        if cursor is not None:
            payload["cursor"] = cursor
        if with_count is not None:
            payload["withCount"] = with_count
        if with_logs is not None:
            payload["withLogs"] = with_logs
        if with_decode is not None:
            payload["withDecode"] = with_decode
        
        return self.client.post(endpoint, payload)

    def is_contract(
        self,
        address: str
    ) -> Dict[str, Any]:
        endpoint = "/v1/kaia/mainnet/blockchain/isContract"
        payload = {"address": address}
        return self.client.post(endpoint, payload)

    def search_events(
        self,
        contract_address: str,
        event_names: List[str],
        abi: Dict[str, Any],
        from_block: Optional[str] = None,
        to_block: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        page: Optional[int] = None,
        rpp: int = 10,
        cursor: Optional[str] = None,
        with_count: Optional[bool] = None
    ) -> Dict[str, Any]:
        endpoint = "/v1/kaia/mainnet/blockchain/searchEvents"
        payload = {
            "contractAddress": contract_address,
            "eventNames": event_names,
            "abi": abi
        }
        
        if from_block is not None:
            payload["fromBlock"] = from_block
        if to_block is not None:
            payload["toBlock"] = to_block
        if from_date is not None:
            payload["fromDate"] = from_date
        if to_date is not None:
            payload["toDate"] = to_date
        if page is not None:
            payload["page"] = page
        if rpp is not None:
            payload["rpp"] = rpp
        if cursor is not None:
            payload["cursor"] = cursor
        if with_count is not None:
            payload["withCount"] = with_count
        
        return self.client.post(endpoint, payload)