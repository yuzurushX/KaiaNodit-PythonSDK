import unittest
import time
from KaiaNoditSDK.blockchain import Blockchain

class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.api_key = "YOUR_NODIT_APIKEY"
        self.blockchain = Blockchain(self.api_key)

    def test_get_block_by_hash_or_number(self):
        block = "172435500"
        response = self.blockchain.get_block_by_hash_or_number(block)
        self.assertIsInstance(response, dict)
        time.sleep(1)  

    def test_get_blocks_within_range(self):
        from_block = "17000000"
        to_block = "17000010" 
        response = self.blockchain.get_blocks_within_range(from_block, to_block)
        self.assertIsInstance(response, dict)
        self.assertIn('items', response)
        self.assertIsInstance(response['items'], list)
        time.sleep(1)

    def test_get_gas_price(self):
        response = self.blockchain.get_gas_price()
        self.assertIsInstance(response, dict)
        time.sleep(1)  

    def test_get_next_nonce_by_account(self):
        account_address = "0x9a50fe055837203a34ed4124dbf6242292a6721f"
        response = self.blockchain.get_next_nonce_by_account(account_address)
        self.assertIsInstance(response, dict)
        time.sleep(1)  


    def test_get_transaction_by_hash(self):
        tx_hash = "0x8c9486689a8780eca3252854a2b936f2462cb5ea43df80c1e7a928f55969a538"
        response = self.blockchain.get_transaction_by_hash(tx_hash)
        self.assertIsInstance(response, dict)
        time.sleep(1)

    def test_get_transactions_by_account(self):
        account_address = "0x9a50fe055837203a34ed4124dbf6242292a6721f"
        page = 1
        rpp = 10
        response = self.blockchain.get_transactions_by_account(
            account_address,
            page=page,
            rpp=rpp
        )
        self.assertIsInstance(response, dict)
        self.assertIn('items', response)
        self.assertIsInstance(response['items'], list)
        time.sleep(1)

    def test_get_transactions_in_block(self):
        block = "172435500"
        page = 1
        rpp = 10
        response = self.blockchain.get_transactions_in_block(
            block,
            page=page,
            rpp=rpp
        )
        self.assertIsInstance(response, dict)
        self.assertIn('items', response)
        self.assertIsInstance(response['items'], list)
        time.sleep(1)  

    def test_is_contract(self):
        address = "0x0f58d0abaae2f586b0d3b6d045305463e89ba603"
        response = self.blockchain.is_contract(address)
        self.assertIsInstance(response, dict)
        time.sleep(1)  

if __name__ == '__main__':
    unittest.main()
