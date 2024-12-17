from typing import Optional, List, Dict, Any
from .client import Client

class NFT:
    def __init__(self, api_key):
        self.client = Client(api_key)

    def get_nft_contract_metadata_by_contracts(
        self, 
        contract_addresses: List[str]
    ) -> Dict[str, Any]:
        endpoint = "/v1/kaia/mainnet/nft/getNftContractMetadataByContracts"
        payload = {"contractAddresses": contract_addresses}
        return self.client.post(endpoint, payload)

    def get_nft_contracts_by_account(
        self, 
        account_address: str, 
        contract_addresses: Optional[List[str]] = None, 
        page: Optional[int] = None, 
        rpp: int = 10,
        cursor: Optional[str] = None, 
        with_count: Optional[bool] = None
    ) -> Dict[str, Any]:
        endpoint = "/v1/kaia/mainnet/nft/getNftContractsByAccount"
        payload = {"accountAddress": account_address}
        
        if contract_addresses is not None:
            payload["contractAddresses"] = contract_addresses
        if page is not None:
            payload["page"] = page
        if rpp is not None:
            payload["rpp"] = rpp
        if cursor is not None:
            payload["cursor"] = cursor
        if with_count is not None:
            payload["withCount"] = with_count
        
        return self.client.post(endpoint, payload)

    def get_nft_holders_by_contract(
        self, 
        contract_address: str, 
        page: Optional[int] = None, 
        rpp: int = 10,
        cursor: Optional[str] = None, 
        with_count: Optional[bool] = None
    ) -> Dict[str, Any]:
        endpoint = "/v1/kaia/mainnet/nft/getNftHoldersByContract"
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

    def get_nft_holders_by_token_id(
        self, 
        contract_address: str, 
        token_id: str, 
        page: Optional[int] = None, 
        rpp: int = 10,
        cursor: Optional[str] = None, 
        with_count: Optional[bool] = None
    ) -> Dict[str, Any]:
        endpoint = "/v1/kaia/mainnet/nft/getNftHoldersByTokenId"
        payload = {
            "contractAddress": contract_address,
            "tokenId": token_id
        }
        
        if page is not None:
            payload["page"] = page
        if rpp is not None:
            payload["rpp"] = rpp
        if cursor is not None:
            payload["cursor"] = cursor
        if with_count is not None:
            payload["withCount"] = with_count
        
        return self.client.post(endpoint, payload)

    def get_nft_metadata_by_contract(
        self, 
        contract_address: str, 
        page: Optional[int] = None, 
        rpp: int = 10,
        cursor: Optional[str] = None, 
        with_count: Optional[bool] = None
    ) -> Dict[str, Any]:
        endpoint = "/v1/kaia/mainnet/nft/getNftMetadataByContract"
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

    def get_nft_metadata_by_token_ids(
        self, 
        tokens: List[Dict[str, str]]
    ) -> Dict[str, Any]:
        endpoint = "/v1/kaia/mainnet/nft/getNftMetadataByTokenIds"
        payload = {"tokens": tokens}
        return self.client.post(endpoint, payload)

    def get_nft_transfers_by_account(
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
        with_count: Optional[bool] = None,
        with_metadata: Optional[bool] = None,
        with_zero_value: Optional[bool] = None
    ) -> Dict[str, Any]:
        endpoint = f"/v1/kaia/mainnet/nft/getNftTransfersByAccount"
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
        if with_metadata is not None:
            payload["withMetadata"] = with_metadata
        if with_zero_value is not None:
            payload["withZeroValue"] = with_zero_value
        
        return self.client.post(endpoint, payload)

    def get_nft_transfers_by_contract(
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
        with_metadata: Optional[bool] = None, 
        with_zero_value: Optional[bool] = None
    ) -> Dict[str, Any]:
        endpoint = "/v1/kaia/mainnet/nft/getNftTransfersByContract"
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
        if with_metadata is not None:
            payload["withMetadata"] = with_metadata
        if with_zero_value is not None:
            payload["withZeroValue"] = with_zero_value
        
        return self.client.post(endpoint, payload)

    def get_nft_transfers_by_token_id(
        self, 
        contract_address: str, 
        token_id: str, 
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
        endpoint = "/v1/kaia/mainnet/nft/getNftTransfersByTokenId"
        payload = {
            "contractAddress": contract_address,
            "tokenId": token_id
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

    def get_nft_transfers_within_range(
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
        endpoint = "/v1/kaia/mainnet/nft/getNftTransfersWithinRange"
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
        if with_metadata is not None:
            payload["withMetadata"] = with_metadata
        if with_zero_value is not None:
            payload["withZeroValue"] = with_zero_value
        
        return self.client.post(endpoint, payload)

    def get_nfts_owned_by_account(
        self, 
        account_address: str, 
        contract_addresses: Optional[List[str]] = None, 
        page: Optional[int] = None, 
        rpp: int = 10,
        cursor: Optional[str] = None, 
        with_count: Optional[bool] = None, 
        with_metadata: Optional[bool] = None
    ) -> Dict[str, Any]:
        endpoint = "/v1/kaia/mainnet/nft/getNftsOwnedByAccount"
        payload = {"accountAddress": account_address}
        
        if contract_addresses is not None:
            payload["contractAddresses"] = contract_addresses
        if page is not None:
            payload["page"] = page
        if rpp is not None:
            payload["rpp"] = rpp
        if cursor is not None:
            payload["cursor"] = cursor
        if with_count is not None:
            payload["withCount"] = with_count
        if with_metadata is not None:
            payload["withMetadata"] = with_metadata
        
        return self.client.post(endpoint, payload)

    def search_nft_contract_metadata_by_keyword(
        self, 
        keyword: str, 
        page: Optional[int] = None, 
        rpp: int = 10,
        cursor: Optional[str] = None, 
        with_count: Optional[bool] = None
    ) -> Dict[str, Any]:
        endpoint = "/v1/kaia/mainnet/nft/searchNftContractMetadataByKeyword"
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