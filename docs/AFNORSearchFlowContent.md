# AFNORSearchFlowContent

A set of flows matching criterias, provided into the request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**filters** | [**AFNORSearchFlowFilters**](AFNORSearchFlowFilters.md) |  | [optional] 
**results** | [**List[AFNORFlow]**](AFNORFlow.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_search_flow_content import AFNORSearchFlowContent

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSearchFlowContent from a JSON string
afnor_search_flow_content_instance = AFNORSearchFlowContent.from_json(json)
# print the JSON string representation of the object
print(AFNORSearchFlowContent.to_json())

# convert the object into a dict
afnor_search_flow_content_dict = afnor_search_flow_content_instance.to_dict()
# create an instance of AFNORSearchFlowContent from a dict
afnor_search_flow_content_from_dict = AFNORSearchFlowContent.from_dict(afnor_search_flow_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


