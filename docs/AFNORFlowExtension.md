# AFNORFlowExtension

Extension schema to build Flow schema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_at** | **datetime** | The last update date and time of the flow. When the flow is submitted updatedAt is equal to submittedAt. When the flow acknowledgment status is changed updatedAt date and time is updated.  | 
**flow_type** | [**AFNORFlowType**](AFNORFlowType.md) |  | 
**processing_rule_source** | **str** | Says whether the processing rule has been computed or the processing rule was an input parameter | 
**flow_direction** | [**AFNORFlowDirection**](AFNORFlowDirection.md) |  | 
**acknowledgement** | [**AFNORAcknowledgement**](AFNORAcknowledgement.md) |  | 

## Example

```python
from factpulse.models.afnor_flow_extension import AFNORFlowExtension

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORFlowExtension from a JSON string
afnor_flow_extension_instance = AFNORFlowExtension.from_json(json)
# print the JSON string representation of the object
print(AFNORFlowExtension.to_json())

# convert the object into a dict
afnor_flow_extension_dict = afnor_flow_extension_instance.to_dict()
# create an instance of AFNORFlowExtension from a dict
afnor_flow_extension_from_dict = AFNORFlowExtension.from_dict(afnor_flow_extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


