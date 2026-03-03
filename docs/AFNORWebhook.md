# AFNORWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_id** | **UUID** |  | [optional] 
**callback** | [**AFNORCallbackParameters**](AFNORCallbackParameters.md) |  | 
**metadata** | [**AFNORWebhookMetadata**](AFNORWebhookMetadata.md) |  | 

## Example

```python
from factpulse.models.afnor_webhook import AFNORWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORWebhook from a JSON string
afnor_webhook_instance = AFNORWebhook.from_json(json)
# print the JSON string representation of the object
print(AFNORWebhook.to_json())

# convert the object into a dict
afnor_webhook_dict = afnor_webhook_instance.to_dict()
# create an instance of AFNORWebhook from a dict
afnor_webhook_from_dict = AFNORWebhook.from_dict(afnor_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


