# WebhookSecretGenerateResponse

Response after generating a webhook secret.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the secret was generated successfully | 
**webhook_secret** | **str** | The generated webhook secret (save it, it will never be shown again) | 
**message** | **str** | Result message | 
**created_at** | **datetime** | When the secret was created | 

## Example

```python
from factpulse.models.webhook_secret_generate_response import WebhookSecretGenerateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSecretGenerateResponse from a JSON string
webhook_secret_generate_response_instance = WebhookSecretGenerateResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookSecretGenerateResponse.to_json())

# convert the object into a dict
webhook_secret_generate_response_dict = webhook_secret_generate_response_instance.to_dict()
# create an instance of WebhookSecretGenerateResponse from a dict
webhook_secret_generate_response_from_dict = WebhookSecretGenerateResponse.from_dict(webhook_secret_generate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


