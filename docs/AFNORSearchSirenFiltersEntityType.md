# AFNORSearchSirenFiltersEntityType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**AFNORStrictOperator**](AFNORStrictOperator.md) |  | [optional] 
**value** | [**AFNOREntityType**](AFNOREntityType.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_search_siren_filters_entity_type import AFNORSearchSirenFiltersEntityType

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSearchSirenFiltersEntityType from a JSON string
afnor_search_siren_filters_entity_type_instance = AFNORSearchSirenFiltersEntityType.from_json(json)
# print the JSON string representation of the object
print(AFNORSearchSirenFiltersEntityType.to_json())

# convert the object into a dict
afnor_search_siren_filters_entity_type_dict = afnor_search_siren_filters_entity_type_instance.to_dict()
# create an instance of AFNORSearchSirenFiltersEntityType from a dict
afnor_search_siren_filters_entity_type_from_dict = AFNORSearchSirenFiltersEntityType.from_dict(afnor_search_siren_filters_entity_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


