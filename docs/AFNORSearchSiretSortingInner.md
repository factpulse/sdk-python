# AFNORSearchSiretSortingInner

A sorting criteria composed of a field and an order (ascending or descending).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | [**AFNORSiretField**](AFNORSiretField.md) |  | [optional] 
**sorting_order** | [**AFNORSortingOrder**](AFNORSortingOrder.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_search_siret_sorting_inner import AFNORSearchSiretSortingInner

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSearchSiretSortingInner from a JSON string
afnor_search_siret_sorting_inner_instance = AFNORSearchSiretSortingInner.from_json(json)
# print the JSON string representation of the object
print(AFNORSearchSiretSortingInner.to_json())

# convert the object into a dict
afnor_search_siret_sorting_inner_dict = afnor_search_siret_sorting_inner_instance.to_dict()
# create an instance of AFNORSearchSiretSortingInner from a dict
afnor_search_siret_sorting_inner_from_dict = AFNORSearchSiretSortingInner.from_dict(afnor_search_siret_sorting_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


