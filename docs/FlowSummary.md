# FlowSummary

Summary of a flow in search results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **str** | Unique flow identifier | 
**tracking_id** | **str** |  | [optional] 
**name** | **str** | Flow name | 
**flow_type** | **str** |  | [optional] 
**flow_direction** | **str** |  | [optional] 
**acknowledgment_status** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from factpulse.models.flow_summary import FlowSummary

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSummary from a JSON string
flow_summary_instance = FlowSummary.from_json(json)
# print the JSON string representation of the object
print(FlowSummary.to_json())

# convert the object into a dict
flow_summary_dict = flow_summary_instance.to_dict()
# create an instance of FlowSummary from a dict
flow_summary_from_dict = FlowSummary.from_dict(flow_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


