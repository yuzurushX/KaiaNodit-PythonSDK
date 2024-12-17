import unittest
import time
from KaiaNoditSDK.statistics import Statistics

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.api_key = "YOUR_NODIT_APIKEY"
        self.statistics = Statistics(self.api_key)

    def test_get_account_stats(self):
        account_address = "0x9a50fe055837203a34ed4124dbf6242292a6721f"
        response = self.statistics.get_account_stats(account_address)
        self.assertIsInstance(response, dict)
        time.sleep(1)  

if __name__ == '__main__':
    unittest.main()