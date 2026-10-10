# AFNORWebhookIdParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_id** | **UUID** |  | [optional] 
**signing_key** | **bytes** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from factpulse.models.afnor_webhook_id_param import AFNORWebhookIdParam

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORWebhookIdParam from a JSON string
afnor_webhook_id_param_instance = AFNORWebhookIdParam.from_json(json)
# print the JSON string representation of the object
print(AFNORWebhookIdParam.to_json())

# convert the object into a dict
afnor_webhook_id_param_dict = afnor_webhook_id_param_instance.to_dict()
# create an instance of AFNORWebhookIdParam from a dict
afnor_webhook_id_param_from_dict = AFNORWebhookIdParam.from_dict(afnor_webhook_id_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


