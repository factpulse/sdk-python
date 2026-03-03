# AFNORWebhookPatchPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | [**List[AFNORCallbackHeader]**](AFNORCallbackHeader.md) |  | [optional] 
**authentication** | [**AFNORCallbackAuthentication**](AFNORCallbackAuthentication.md) |  | [optional] 
**signature** | [**AFNORCallbackSignature**](AFNORCallbackSignature.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_webhook_patch_payload import AFNORWebhookPatchPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORWebhookPatchPayload from a JSON string
afnor_webhook_patch_payload_instance = AFNORWebhookPatchPayload.from_json(json)
# print the JSON string representation of the object
print(AFNORWebhookPatchPayload.to_json())

# convert the object into a dict
afnor_webhook_patch_payload_dict = afnor_webhook_patch_payload_instance.to_dict()
# create an instance of AFNORWebhookPatchPayload from a dict
afnor_webhook_patch_payload_from_dict = AFNORWebhookPatchPayload.from_dict(afnor_webhook_patch_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


