from .nft import NFT
from .token import Token
from .client import Client
from .blockchain import Blockchain
from .statistics import Statistics
        
class KaiaNoditSDK:
    def __init__(self, api_key):
        self.nft = NFT(api_key)
        self.token = Token(api_key)
        self.blockchain = Blockchain(api_key)
        self.statistics = Statistics(api_key)

__all__ = ['NFT', 'Token', 'Client', 'Blockchain', 'Statistics']