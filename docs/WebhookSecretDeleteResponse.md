# WebhookSecretDeleteResponse

Response after deleting webhook secret.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the secret was deleted successfully | 
**message** | **str** | Result message | 

## Example

```python
from factpulse.models.webhook_secret_delete_response import WebhookSecretDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSecretDeleteResponse from a JSON string
webhook_secret_delete_response_instance = WebhookSecretDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookSecretDeleteResponse.to_json())

# convert the object into a dict
webhook_secret_delete_response_dict = webhook_secret_delete_response_instance.to_dict()
# create an instance of WebhookSecretDeleteResponse from a dict
webhook_secret_delete_response_from_dict = WebhookSecretDeleteResponse.from_dict(webhook_secret_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


