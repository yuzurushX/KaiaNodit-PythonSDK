import unittest
from KaiaNoditSDK.token import Token    
import time

class TestToken(unittest.TestCase):
    def setUp(self):
        self.api_key = "YOUR_NODIT_APIKEY"
        self.token = Token(self.api_key)

    def test_get_native_balance_by_account(self):
        account_address = "0x9a50fe055837203a34ed4124dbf6242292a6721f"
        response = self.token.get_native_balance_by_account(account_address)
        self.assertIsInstance(response, dict) 
        time.sleep(1)  

    def test_get_token_transfers_by_contract(self):
        contract_address = "0x0f58d0abaae2f586b0d3b6d045305463e89ba603"
        response = self.token.get_token_transfers_by_contract(contract_address)
        self.assertIsInstance(response, dict)
        time.sleep(1)
    def test_get_token_transfers_by_account(self):
        account_address = "0x9a50fe055837203a34ed4124dbf6242292a6721f"
        response = self.token.get_token_transfers_by_account(account_address)
        self.assertIsInstance(response, dict)
        self.assertIn('items', response)
        self.assertIsInstance(response['items'], list)
        time.sleep(1)  

    def test_get_token_contract_metadata_by_contracts(self):
        contract_addresses = ["0x0f58d0abaae2f586b0d3b6d045305463e89ba603", "0x754288077d0ff82af7a5317c7cb8c444d421d103"]
        response = self.token.get_token_contract_metadata_by_contracts(contract_addresses)
        self.assertIsInstance(response, list)
        self.assertTrue(all(isinstance(item, dict) for item in response))
        time.sleep(1)  

    def test_get_token_holders_by_contract(self):
        contract_address = "0x0f58d0abaae2f586b0d3b6d045305463e89ba603"
        response = self.token.get_token_holders_by_contract(contract_address)
        self.assertIsInstance(response, dict)
        self.assertIn('items', response)
        self.assertIsInstance(response['items'], list)
        time.sleep(1)  

    def test_get_tokens_owned_by_account(self):
        account_address = "0x9a50fe055837203a34ed4124dbf6242292a6721f"
        response = self.token.get_tokens_owned_by_account(account_address)
        self.assertIsInstance(response, dict)
        self.assertIn('items', response)
        self.assertIsInstance(response['items'], list)
        time.sleep(1)  



if __name__ == '__main__':
    unittest.main()