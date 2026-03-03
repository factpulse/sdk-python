# AFNORFlow

The properties of a Flow resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_id** | **str** | The tracking id is an external identifier and is used to track the flow by the sender | [optional] 
**name** | **str** | Name of the file | 
**processing_rule** | [**AFNORProcessingRule**](AFNORProcessingRule.md) |  | [optional] 
**flow_syntax** | [**AFNORFlowSyntax**](AFNORFlowSyntax.md) |  | 
**flow_profile** | [**AFNORFlowProfile**](AFNORFlowProfile.md) |  | [optional] 
**flow_id** | **str** | Unique identifier supporting UUID but not only, for flexibility purpose | 
**submitted_at** | **datetime** | The flow submission date and time (the date and time when the flow was created on the system) This property should be used by the API consumer as a time reference to avoid clock synchronization issues  | 
**updated_at** | **datetime** | The last update date and time of the flow. When the flow is submitted updatedAt is equal to submittedAt. When the flow acknowledgment status is changed updatedAt date and time is updated.  | 
**flow_type** | [**AFNORFlowType**](AFNORFlowType.md) |  | 
**processing_rule_source** | **str** | Says whether the processing rule has been computed or the processing rule was an input parameter | 
**flow_direction** | [**AFNORFlowDirection**](AFNORFlowDirection.md) |  | 
**acknowledgement** | [**AFNORAcknowledgement**](AFNORAcknowledgement.md) |  | 

## Example

```python
from factpulse.models.afnor_flow import AFNORFlow

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORFlow from a JSON string
afnor_flow_instance = AFNORFlow.from_json(json)
# print the JSON string representation of the object
print(AFNORFlow.to_json())

# convert the object into a dict
afnor_flow_dict = afnor_flow_instance.to_dict()
# create an instance of AFNORFlow from a dict
afnor_flow_from_dict = AFNORFlow.from_dict(afnor_flow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


