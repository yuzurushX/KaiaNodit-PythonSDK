import unittest
import time
from KaiaNoditSDK.nft import NFT

class TestNFT(unittest.TestCase):
    def setUp(self):
        self.api_key = "YOUR_NODIT_APIKEY"
        self.nft = NFT(self.api_key)

    def test_get_nft_contract_metadata_by_contracts(self):
        contract_addresses = ["0x8e4deb5c901ef81f43f6ca83a0fed5689cfdced3", "0x898f2afc07924f5a4f9612449e4c4f8eca527515"]
        response = self.nft.get_nft_contract_metadata_by_contracts(contract_addresses)
        self.assertIsInstance(response, list)  
        self.assertTrue(all(isinstance(item, dict) for item in response)) 
        time.sleep(1)  

    def test_get_nft_contracts_by_account(self):
        account_address = "0xe06670f6852de86c19e8ece42062c2640ccad001"
        response = self.nft.get_nft_contracts_by_account(account_address)
        self.assertIsInstance(response, dict)  # Example assertion
        time.sleep(1)  

    def test_get_nft_holders_by_contract(self):
        contract_address = "0x8e4deb5c901ef81f43f6ca83a0fed5689cfdced3"
        response = self.nft.get_nft_holders_by_contract(contract_address)
        self.assertIsInstance(response, dict)
        self.assertIn('items', response)
        self.assertIsInstance(response['items'], list)
        time.sleep(1)  

    def test_get_nft_transfers_by_account(self):
        account_address = "0xe06670f6852de86c19e8ece42062c2640ccad001"
        response = self.nft.get_nft_transfers_by_account(account_address)
        self.assertIsInstance(response, dict)
        self.assertIn('items', response)
        self.assertIsInstance(response['items'], list)
        time.sleep(1)  

    def test_get_nft_transfers_by_contract(self):
        contract_address = "0x8e4deb5c901ef81f43f6ca83a0fed5689cfdced3"
        response = self.nft.get_nft_transfers_by_contract(contract_address)
        self.assertIsInstance(response, dict)
        self.assertIn('items', response)
        self.assertIsInstance(response['items'], list)
        time.sleep(2)  

    def test_get_nft_transfers_within_range(self):
        from_block = "0"
        to_block = "latest"
        response = self.nft.get_nft_transfers_within_range(from_block, to_block)
        self.assertIsInstance(response, dict)
        self.assertIn('items', response)
        self.assertIsInstance(response['items'], list)
        time.sleep(2)  

    def test_get_nfts_owned_by_account(self):
        account_address = "0xc30dffb7eaeda1bf31344f902d2e2b5938553a35"
        response = self.nft.get_nfts_owned_by_account(account_address, rpp=5)
        self.assertIsInstance(response, dict)
        self.assertIn('items', response)
        self.assertIsInstance(response['items'], list)
        time.sleep(2)  


if __name__ == '__main__':
    unittest.main()