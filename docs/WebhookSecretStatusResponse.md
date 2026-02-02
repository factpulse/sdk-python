# WebhookSecretStatusResponse

Webhook secret status for a client.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_secret** | **bool** | Whether a webhook secret is configured | 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from factpulse.models.webhook_secret_status_response import WebhookSecretStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSecretStatusResponse from a JSON string
webhook_secret_status_response_instance = WebhookSecretStatusResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookSecretStatusResponse.to_json())

# convert the object into a dict
webhook_secret_status_response_dict = webhook_secret_status_response_instance.to_dict()
# create an instance of WebhookSecretStatusResponse from a dict
webhook_secret_status_response_from_dict = WebhookSecretStatusResponse.from_dict(webhook_secret_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


