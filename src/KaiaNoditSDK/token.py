from typing import Optional, List, Dict, Any
from .client import Client

class Token:
    def __init__(self, api_key, network="mainnet"):
        self.client = Client(api_key)
        self.network = network
        self.base_path = f"/v1/kaia/{network if network == 'mainnet' else 'kairos'}"

    def get_native_balance_by_account(
        self, 
        account_address: str
    ) -> Dict[str, Any]:
        endpoint = f"{self.base_path}/native/getNativeBalanceByAccount"
        payload = {"accountAddress": account_address}
        return self.client.post(endpoint, payload)

    def get_token_prices_by_contracts(
        self, 
        contract_addresses: List[str],
        currency: Optional[str] = None
    ) -> Dict[str, Any]:
        endpoint = f"{self.base_path}/token/getTokenPricesByContracts"
        payload = {"contractAddresses": contract_addresses}
        
        if currency is not None:
            payload["currency"] = currency
        
        return self.client.post(endpoint, payload)

    def get_token_transfers_by_account(
        self, 
        account_address: str, 
        relation: Optional[str] = None, 
        contract_addresses: Optional[List[str]] = None, 
        from_block: Optional[str] = None, 
        to_block: Optional[str] = None, 
        from_date: Optional[str] = None, 
        to_date: Optional[str] = None, 
        page: Optional[int] = None, 
        rpp: int = 10, 
        cursor: Optional[str] = None, 
        with_count: Optional[bool] = None
    ) -> Dict[str, Any]:
        endpoint = f"{self.base_path}/token/getTokenTransfersByAccount"
        payload = {"accountAddress": account_address}
        
        if relation is not None:
            payload["relation"] = relation
        if contract_addresses is not None:
            payload["contractAddresses"] = contract_addresses
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

    def get_token_allowance(
        self, 
        contract_address: str, 
        owner_address: str, 
        spender_address: str
    ) -> Dict[str, Any]:
        endpoint = f"{self.base_path}/token/getTokenAllowance"
        payload = {
            "contractAddress": contract_address,
            "ownerAddress": owner_address,
            "spenderAddress": spender_address
        }
        return self.client.post(endpoint, payload)

    def get_token_contract_metadata_by_contracts(
        self, 
        contract_addresses: List[str]
    ) -> Dict[str, Any]:
        endpoint = f"{self.base_path}/token/getTokenContractMetadataByContracts"
        payload = {"contractAddresses": contract_addresses}
        return self.client.post(endpoint, payload)

    def get_token_holders_by_contract(
        self, 
        contract_address: str, 
        page: Optional[int] = None, 
        rpp: int = 10, 
        cursor: Optional[str] = None, 
        with_count: Optional[bool] = None
    ) -> Dict[str, Any]:
        endpoint = f"{self.base_path}/token/getTokenHoldersByContract"
        payload = {"contractAddress": contract_address}
        
        if page is not None:
            payload["page"] = page
        if rpp is not None: 
            payload["rpp"] = rpp
        if cursor is not None:
            payload["cursor"] = cursor
        if with_count is not None:
            payload["withCount"] = with_count
        
        return self.client.post(endpoint, payload)

    def get_token_transfers_by_contract(
        self, 
        contract_address: str, 
        from_block: Optional[str] = None, 
        to_block: Optional[str] = None, 
        from_date: Optional[str] = None, 
        to_date: Optional[str] = None, 
        page: Optional[int] = None, 
        rpp: int = 10, 
        cursor: Optional[str] = None, 
        with_count: Optional[bool] = None, 
        with_zero_value: Optional[bool] = None
    ) -> Dict[str, Any]:
        endpoint = f"{self.base_path}/token/getTokenTransfersByContract"
        payload = {"contractAddress": contract_address}
        
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
        if with_zero_value is not None:
            payload["withZeroValue"] = with_zero_value
        
        return self.client.post(endpoint, payload)

    def get_token_transfers_within_range(
        self, 
        from_block: Optional[str] = None, 
        to_block: Optional[str] = None, 
        from_date: Optional[str] = None, 
        to_date: Optional[str] = None, 
        page: Optional[int] = None, 
        rpp: int = 10, 
        cursor: Optional[str] = None, 
        with_count: Optional[bool] = None, 
        with_metadata: Optional[bool] = None, 
        with_zero_value: Optional[bool] = None
    ) -> Dict[str, Any]:
        endpoint = f"{self.base_path}/token/getTokenTransfersWithinRange"
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
        if rpp != 10:
            payload["rpp"] = rpp
        if cursor is not None:
            payload["cursor"] = cursor
        if with_count is not None:
            payload["withCount"] = with_count
        if with_metadata is not None:
            payload["withMetadata"] = with_metadata
        if with_zero_value is not None:
            payload["withZeroValue"] = with_zero_value
        
        return self.client.post(endpoint, payload)

    def get_tokens_owned_by_account(
        self, 
        account_address: str, 
        contract_address: Optional[str] = None, 
        page: Optional[int] = None, 
        rpp: int = 10, 
        cursor: Optional[str] = None, 
        with_count: Optional[bool] = None
    ) -> Dict[str, Any]:
        endpoint = f"{self.base_path}/token/getTokensOwnedByAccount"
        payload = {"accountAddress": account_address}
        
        if contract_address is not None:
            payload["contractAddress"] = contract_address
        if page is not None:
            payload["page"] = page
        if rpp is not None:
            payload["rpp"] = rpp
        if cursor is not None:
            payload["cursor"] = cursor
        if with_count is not None:
            payload["withCount"] = with_count
            
        return self.client.post(endpoint, payload)

    def search_token_contract_metadata_by_keyword(
        self, 
        keyword: str, 
        page: Optional[int] = None, 
        rpp: int = 10, 
        cursor: Optional[str] = None, 
        with_count: Optional[bool] = None
    ) -> Dict[str, Any]:
        endpoint = f"{self.base_path}/token/searchTokenContractMetadataByKeyword"
        payload = {"keyword": keyword}
        
        if page is not None:
            payload["page"] = page
        if rpp is not None:
            payload["rpp"] = rpp
        if cursor is not None:
            payload["cursor"] = cursor
        if with_count is not None:
            payload["withCount"] = with_count
        
        return self.client.post(endpoint, payload)    