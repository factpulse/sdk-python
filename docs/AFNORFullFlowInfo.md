# AFNORFullFlowInfo

Identified Flow info: flow info + id + timestamp

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_id** | **str** | Unique identifier supporting UUID but not only, for flexibility purpose | [optional] 
**name** | **str** | Name of the file | [optional] 
**processing_rule** | [**AFNORProcessingRule**](AFNORProcessingRule.md) |  | [optional] 
**flow_syntax** | [**AFNORFlowSyntax**](AFNORFlowSyntax.md) |  | 
**flow_profile** | [**AFNORFlowProfile**](AFNORFlowProfile.md) |  | [optional] 
**sha256** | **str** |  | [optional] 
**flow_id** | **str** | Unique identifier supporting UUID but not only, for flexibility purpose | [optional] 
**submitted_at** | **datetime** | The flow submission date and time (the date and time when the flow was created on the system) This property should be used by the API consumer as a time reference to avoid clock synchronization issues  | [optional] 

## Example

```python
from factpulse.models.afnor_full_flow_info import AFNORFullFlowInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORFullFlowInfo from a JSON string
afnor_full_flow_info_instance = AFNORFullFlowInfo.from_json(json)
# print the JSON string representation of the object
print(AFNORFullFlowInfo.to_json())

# convert the object into a dict
afnor_full_flow_info_dict = afnor_full_flow_info_instance.to_dict()
# create an instance of AFNORFullFlowInfo from a dict
afnor_full_flow_info_from_dict = AFNORFullFlowInfo.from_dict(afnor_full_flow_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


