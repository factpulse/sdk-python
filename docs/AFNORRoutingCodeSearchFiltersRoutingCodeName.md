# AFNORRoutingCodeSearchFiltersRoutingCodeName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**AFNORContainsOperator**](AFNORContainsOperator.md) |  | [optional] 
**value** | **str** | Name of the routing code. | [optional] 

## Example

```python
from factpulse.models.afnor_routing_code_search_filters_routing_code_name import AFNORRoutingCodeSearchFiltersRoutingCodeName

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORRoutingCodeSearchFiltersRoutingCodeName from a JSON string
afnor_routing_code_search_filters_routing_code_name_instance = AFNORRoutingCodeSearchFiltersRoutingCodeName.from_json(json)
# print the JSON string representation of the object
print(AFNORRoutingCodeSearchFiltersRoutingCodeName.to_json())

# convert the object into a dict
afnor_routing_code_search_filters_routing_code_name_dict = afnor_routing_code_search_filters_routing_code_name_instance.to_dict()
# create an instance of AFNORRoutingCodeSearchFiltersRoutingCodeName from a dict
afnor_routing_code_search_filters_routing_code_name_from_dict = AFNORRoutingCodeSearchFiltersRoutingCodeName.from_dict(afnor_routing_code_search_filters_routing_code_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


