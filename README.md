# KaiaNodit-PythonSDK

A Python SDK for interacting with the Nodit API to access Kaia Chain blockchain data.

## Installation 

```bash
python setup.py sdist bdist_wheel
pip install dist/KaiaNoditSDK-0.1.0-py3-none-any.whl
```

## Usage

```python
from KaiaNoditSDK import KaiaNoditSDK


api_key = "YOUR_NODIT_APIKEY"
sdk = KaiaNoditSDK(api_key)
``` 

## Tests

To run the tests, use the following command:

```bash
pytest tests
```
