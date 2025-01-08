# KaiaNodit-PythonSDK

A Python SDK for interacting with the Nodit API to access Kaia Chain blockchain data. This SDK provides easy access to Node API and Webhook functionality for seamless blockchain integration.

## Features
- 🌐 Web3 API Functionality
- 🔗 Node API Integration
- 🔌 Webhook API Support
- 🌐 Multiple Network Support (Mainnet & Testnet)

## Installation

You can install the package directly from the source:

```bash
python setup.py sdist bdist_wheel
pip install dist/KaiaNoditSDK-0.1.0-py3-none-any.whl
```

## Quick Start

```python
from KaiaNoditSDK import KaiaNoditSDK
```

Initialize the SDK with your API key (default is mainnet)
```python
api_key = "YOUR_NODIT_APIKEY"
sdk = KaiaNoditSDK(api_key)
```
For testnet usage
```python
testnet_sdk = KaiaNoditSDK(api_key, network="testnet")
```

## Documentation

For detailed API documentation, visit [Nodit API Documentation](https://developer.nodit.io/reference/kaia-quickstart).
