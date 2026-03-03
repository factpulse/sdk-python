# AFNORCoreFlowInfo

Core schema to build FlowInfo, FullFlowInfo, Flow schemas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_id** | **str** | The tracking id is an external identifier and is used to track the flow by the sender | [optional] 
**name** | **str** | Name of the file | 
**processing_rule** | [**AFNORProcessingRule**](AFNORProcessingRule.md) |  | [optional] 
**flow_syntax** | [**AFNORFlowSyntax**](AFNORFlowSyntax.md) |  | 
**flow_profile** | [**AFNORFlowProfile**](AFNORFlowProfile.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_core_flow_info import AFNORCoreFlowInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORCoreFlowInfo from a JSON string
afnor_core_flow_info_instance = AFNORCoreFlowInfo.from_json(json)
# print the JSON string representation of the object
print(AFNORCoreFlowInfo.to_json())

# convert the object into a dict
afnor_core_flow_info_dict = afnor_core_flow_info_instance.to_dict()
# create an instance of AFNORCoreFlowInfo from a dict
afnor_core_flow_info_from_dict = AFNORCoreFlowInfo.from_dict(afnor_core_flow_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


