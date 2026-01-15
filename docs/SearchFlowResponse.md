# SearchFlowResponse

Response from a flow search.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total number of results | 
**offset** | **int** | Applied offset | 
**limit** | **int** | Results limit | 
**results** | [**List[FlowSummary]**](FlowSummary.md) | List of found flows | 

## Example

```python
from factpulse.models.search_flow_response import SearchFlowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFlowResponse from a JSON string
search_flow_response_instance = SearchFlowResponse.from_json(json)
# print the JSON string representation of the object
print(SearchFlowResponse.to_json())

# convert the object into a dict
search_flow_response_dict = search_flow_response_instance.to_dict()
# create an instance of SearchFlowResponse from a dict
search_flow_response_from_dict = SearchFlowResponse.from_dict(search_flow_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


