# AFNORFullFlowInfoExtension

Extension schema to build FFullFlowInfo, Flow schemas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **str** | Unique identifier supporting UUID but not only, for flexibility purpose | 
**submitted_at** | **datetime** | The flow submission date and time (the date and time when the flow was created on the system) This property should be used by the API consumer as a time reference to avoid clock synchronization issues  | 

## Example

```python
from factpulse.models.afnor_full_flow_info_extension import AFNORFullFlowInfoExtension

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORFullFlowInfoExtension from a JSON string
afnor_full_flow_info_extension_instance = AFNORFullFlowInfoExtension.from_json(json)
# print the JSON string representation of the object
print(AFNORFullFlowInfoExtension.to_json())

# convert the object into a dict
afnor_full_flow_info_extension_dict = afnor_full_flow_info_extension_instance.to_dict()
# create an instance of AFNORFullFlowInfoExtension from a dict
afnor_full_flow_info_extension_from_dict = AFNORFullFlowInfoExtension.from_dict(afnor_full_flow_info_extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


