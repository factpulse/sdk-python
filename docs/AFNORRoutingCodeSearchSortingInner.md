# AFNORRoutingCodeSearchSortingInner

A sort criteria composed of a field and an order (ascending or descending).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | [**AFNORRoutingCodeField**](AFNORRoutingCodeField.md) |  | [optional] 
**order** | [**AFNORSortingOrder**](AFNORSortingOrder.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_routing_code_search_sorting_inner import AFNORRoutingCodeSearchSortingInner

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORRoutingCodeSearchSortingInner from a JSON string
afnor_routing_code_search_sorting_inner_instance = AFNORRoutingCodeSearchSortingInner.from_json(json)
# print the JSON string representation of the object
print(AFNORRoutingCodeSearchSortingInner.to_json())

# convert the object into a dict
afnor_routing_code_search_sorting_inner_dict = afnor_routing_code_search_sorting_inner_instance.to_dict()
# create an instance of AFNORRoutingCodeSearchSortingInner from a dict
afnor_routing_code_search_sorting_inner_from_dict = AFNORRoutingCodeSearchSortingInner.from_dict(afnor_routing_code_search_sorting_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


