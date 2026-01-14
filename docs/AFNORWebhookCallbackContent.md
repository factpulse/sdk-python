# AFNORWebhookCallbackContent



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_info** | [**AFNORFlow**](AFNORFlow.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_webhook_callback_content import AFNORWebhookCallbackContent

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORWebhookCallbackContent from a JSON string
afnor_webhook_callback_content_instance = AFNORWebhookCallbackContent.from_json(json)
# print the JSON string representation of the object
print(AFNORWebhookCallbackContent.to_json())

# convert the object into a dict
afnor_webhook_callback_content_dict = afnor_webhook_callback_content_instance.to_dict()
# create an instance of AFNORWebhookCallbackContent from a dict
afnor_webhook_callback_content_from_dict = AFNORWebhookCallbackContent.from_dict(afnor_webhook_callback_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


