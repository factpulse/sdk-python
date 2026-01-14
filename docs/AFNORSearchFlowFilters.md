# AFNORSearchFlowFilters

Filtering criteria, at least one is required

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_after** | **datetime** |  | [optional] 
**updated_before** | **datetime** |  | [optional] 
**processing_rule** | [**List[AFNORProcessingRule]**](AFNORProcessingRule.md) |  | [optional] 
**flow_type** | [**List[AFNORFlowType]**](AFNORFlowType.md) |  | [optional] 
**flow_direction** | [**List[AFNORFlowDirection]**](AFNORFlowDirection.md) |  | [optional] 
**tracking_id** | **str** | Unique identifier supporting UUID but not only, for flexibility purpose | [optional] 
**ack_status** | [**AFNORFlowAckStatus**](AFNORFlowAckStatus.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_search_flow_filters import AFNORSearchFlowFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSearchFlowFilters from a JSON string
afnor_search_flow_filters_instance = AFNORSearchFlowFilters.from_json(json)
# print the JSON string representation of the object
print(AFNORSearchFlowFilters.to_json())

# convert the object into a dict
afnor_search_flow_filters_dict = afnor_search_flow_filters_instance.to_dict()
# create an instance of AFNORSearchFlowFilters from a dict
afnor_search_flow_filters_from_dict = AFNORSearchFlowFilters.from_dict(afnor_search_flow_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


