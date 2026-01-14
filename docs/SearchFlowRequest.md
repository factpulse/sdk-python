# SearchFlowRequest

Request to search submitted flows.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_after** | **datetime** |  | [optional] 
**updated_before** | **datetime** |  | [optional] 
**flow_types** | [**List[FlowType]**](FlowType.md) |  | [optional] 
**flow_directions** | [**List[FlowDirection]**](FlowDirection.md) |  | [optional] 
**tracking_id** | **str** |  | [optional] 
**flow_id** | **str** |  | [optional] 
**acknowledgment_status** | [**AcknowledgmentStatus**](AcknowledgmentStatus.md) |  | [optional] 
**offset** | **int** | Offset for pagination | [optional] [default to 0]
**limit** | **int** | Maximum number of results (max 100) | [optional] [default to 25]

## Example

```python
from factpulse.models.search_flow_request import SearchFlowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFlowRequest from a JSON string
search_flow_request_instance = SearchFlowRequest.from_json(json)
# print the JSON string representation of the object
print(SearchFlowRequest.to_json())

# convert the object into a dict
search_flow_request_dict = search_flow_request_instance.to_dict()
# create an instance of SearchFlowRequest from a dict
search_flow_request_from_dict = SearchFlowRequest.from_dict(search_flow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


