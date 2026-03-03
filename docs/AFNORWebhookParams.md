# AFNORWebhookParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback** | [**AFNORCallbackParameters**](AFNORCallbackParameters.md) |  | 
**metadata** | [**AFNORWebhookMetadata**](AFNORWebhookMetadata.md) |  | 

## Example

```python
from factpulse.models.afnor_webhook_params import AFNORWebhookParams

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORWebhookParams from a JSON string
afnor_webhook_params_instance = AFNORWebhookParams.from_json(json)
# print the JSON string representation of the object
print(AFNORWebhookParams.to_json())

# convert the object into a dict
afnor_webhook_params_dict = afnor_webhook_params_instance.to_dict()
# create an instance of AFNORWebhookParams from a dict
afnor_webhook_params_from_dict = AFNORWebhookParams.from_dict(afnor_webhook_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


