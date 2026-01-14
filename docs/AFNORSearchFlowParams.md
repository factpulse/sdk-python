# AFNORSearchFlowParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Maximum number of results that may be returned | [optional] [default to 25]
**where** | [**AFNORSearchFlowFilters**](AFNORSearchFlowFilters.md) |  | 

## Example

```python
from factpulse.models.afnor_search_flow_params import AFNORSearchFlowParams

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSearchFlowParams from a JSON string
afnor_search_flow_params_instance = AFNORSearchFlowParams.from_json(json)
# print the JSON string representation of the object
print(AFNORSearchFlowParams.to_json())

# convert the object into a dict
afnor_search_flow_params_dict = afnor_search_flow_params_instance.to_dict()
# create an instance of AFNORSearchFlowParams from a dict
afnor_search_flow_params_from_dict = AFNORSearchFlowParams.from_dict(afnor_search_flow_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


