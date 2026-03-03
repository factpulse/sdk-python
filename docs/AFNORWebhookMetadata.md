# AFNORWebhookMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processing_rule** | [**AFNORProcessingRule**](AFNORProcessingRule.md) |  | [optional] 
**flow_type** | [**AFNORFlowType**](AFNORFlowType.md) |  | 
**flow_direction** | [**AFNORFlowDirection**](AFNORFlowDirection.md) |  | 
**ack_status** | [**AFNORFlowAckStatus**](AFNORFlowAckStatus.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_webhook_metadata import AFNORWebhookMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORWebhookMetadata from a JSON string
afnor_webhook_metadata_instance = AFNORWebhookMetadata.from_json(json)
# print the JSON string representation of the object
print(AFNORWebhookMetadata.to_json())

# convert the object into a dict
afnor_webhook_metadata_dict = afnor_webhook_metadata_instance.to_dict()
# create an instance of AFNORWebhookMetadata from a dict
afnor_webhook_metadata_from_dict = AFNORWebhookMetadata.from_dict(afnor_webhook_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


