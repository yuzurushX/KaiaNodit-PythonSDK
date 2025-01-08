from enum import Enum
from typing import List, Optional, Union
from .client import Client
from datetime import datetime

class WebhookEventType(Enum):
    ADDRESS_ACTIVITY = "ADDRESS_ACTIVITY"
    MINED_TRANSACTION = "MINED_TRANSACTION"
    SUCCESSFUL_TRANSACTION = "SUCCESSFUL_TRANSACTION"
    FAILED_TRANSACTION = "FAILED_TRANSACTION"
    TOKEN_TRANSFER = "TOKEN_TRANSFER"
    BELOW_THRESHOLD_BALANCE = "BELOW_THRESHOLD_BALANCE"
    BLOCK_PERIOD = "BLOCK_PERIOD"
    BLOCK_LIST_CALLER = "BLOCK_LIST_CALLER"
    ALLOW_LIST_CALLER = "ALLOW_LIST_CALLER"
    LOG = "LOG"

class WebhookStatus(Enum):
    SUCCESS = "SUCCESS"
    FAIL = "FAIL"

class Webhook:
    def __init__(self, api_key: str, network: str = "mainnet"):
        self.client = Client(api_key)
        self.network = network
        self.base_endpoint = f"/v1/kaia/{network}/webhooks"

    def get_webhooks(self, subscription_id: str, page: Optional[int] = None, rpp: Optional[int] = None) -> dict:
        params = {"subscriptionId": subscription_id}
        if page is not None:
            params["page"] = str(page)  # Convert to string as URL parameters
        if rpp is not None:
            params["rpp"] = str(rpp)  # Convert to string as URL parameters
            
        return self.client.get(self.base_endpoint, params=params)

    def create_webhook(self, 
                      event_type: Union[WebhookEventType, str],
                      webhook_url: str,
                      description: str,
                      condition: dict) -> dict:

        if isinstance(event_type, WebhookEventType):
            event_type = event_type.value

        payload = {
            "eventType": event_type,
            "description": description,
            "notification": {
                "webhookUrl": webhook_url
            },
            "condition": condition
        }

        return self.client.post(self.base_endpoint, payload)

    def create_address_activity_webhook(self, webhook_url: str, addresses: List[str], description: str) -> dict:
        condition = {"addresses": addresses}
        return self.create_webhook(WebhookEventType.ADDRESS_ACTIVITY, webhook_url, description, condition)

    def create_token_transfer_webhook(self, webhook_url: str, token_addresses: List[str], description: str) -> dict:
        condition = {"tokens": [{"contractAddress": addr} for addr in token_addresses]}
        return self.create_webhook(WebhookEventType.TOKEN_TRANSFER, webhook_url, description, condition)

    def create_balance_threshold_webhook(self, webhook_url: str, address: str, 
                                       threshold_balance: str, description: str) -> dict:
        condition = {
            "address": address,
            "belowThresholdBalance": threshold_balance
        }
        return self.create_webhook(WebhookEventType.BELOW_THRESHOLD_BALANCE, webhook_url, description, condition)

    def create_block_period_webhook(self, webhook_url: str, period: int, description: str) -> dict:
        condition = {"period": period}
        return self.create_webhook(WebhookEventType.BLOCK_PERIOD, webhook_url, description, condition)

    def create_block_list_caller_webhook(self, webhook_url: str, address: str, 
                                       block_list_callers: List[str], description: str) -> dict:
        condition = {
            "address": address,
            "blockListCallers": block_list_callers
        }
        return self.create_webhook(WebhookEventType.BLOCK_LIST_CALLER, webhook_url, description, condition)

    def create_log_webhook(self, webhook_url: str, address: str, 
                          topics: List[str], description: str) -> dict:
        condition = {
            "address": address,
            "topics": topics
        }
        return self.create_webhook(WebhookEventType.LOG, webhook_url, description, condition)

    def update_webhook(self, 
                      webhook_id: str,
                      webhook_url: Optional[str] = None,
                      description: Optional[str] = None,
                      is_active: Optional[bool] = None,
                      condition: Optional[dict] = None) -> dict:
        if not webhook_id:
            raise ValueError("webhook_id is required")

        payload = {}
        
        if webhook_url:
            payload["notification"] = {"webhookUrl": webhook_url}
        if description is not None:
            payload["description"] = description
        if is_active is not None:
            payload["isActive"] = is_active
        if condition is not None:
            payload["condition"] = condition
        
        endpoint = f"{self.base_endpoint}/{webhook_id}"
        return self.client.patch(endpoint, payload)

    def delete_webhook(self, webhook_id: str) -> dict:
        if not webhook_id:
            raise ValueError("webhook_id is required")
            
        endpoint = f"{self.base_endpoint}/{webhook_id}"
        return self.client.delete(endpoint)

    def get_webhook_history(
        self,
        subscription_id: str,
        page: Optional[int] = None,
        rpp: Optional[int] = None,
        with_event_message: Optional[bool] = None,
        status: Optional[Union[WebhookStatus, str]] = None,
        start_at: Optional[Union[datetime, str]] = None,
        end_at: Optional[Union[datetime, str]] = None,
        start_sequence_number: Optional[str] = None
    ) -> dict:

        if not subscription_id:
            raise ValueError("subscription_id is required")

        params = {"subscriptionId": subscription_id}

        if page is not None:
            params["page"] = str(page)
        if rpp is not None:
            params["rpp"] = str(rpp)
        if with_event_message is not None:
            params["withEventMessage"] = str(with_event_message).lower()
        if status is not None:
            params["status"] = status.value if isinstance(status, WebhookStatus) else status
        if start_at is not None:
            if isinstance(start_at, datetime):
                params["startAt"] = start_at.isoformat()
            else:
                params["startAt"] = start_at
        if end_at is not None:
            if isinstance(end_at, datetime):
                params["endAt"] = end_at.isoformat()
            else:
                params["endAt"] = end_at
        if start_sequence_number is not None:
            params["startSequenceNumber"] = start_sequence_number

        endpoint = f"{self.base_endpoint}/history"
        return self.client.get(endpoint, params=params)

        
