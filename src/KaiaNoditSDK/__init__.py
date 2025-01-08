from .nft import NFT
from .token import Token
from .client import Client
from .blockchain import Blockchain
from .statistics import Statistics
from .node import Node
from .webhook import Webhook

class KaiaNoditSDK:
    def __init__(self, api_key, network="mainnet"):
        self.nft = NFT(api_key, network)
        self.token = Token(api_key, network)
        self.blockchain = Blockchain(api_key, network)
        self.statistics = Statistics(api_key, network)
        self.node = Node(api_key, network)
        self.webhook = Webhook(api_key, network)

__all__ = ['NFT', 'Token', 'Client', 'Blockchain', 'Statistics', 'Node', 'Webhook']