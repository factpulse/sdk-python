# AFNORSearchSiretFiltersName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**AFNORContainsOperator**](AFNORContainsOperator.md) |  | [optional] 
**value** | **str** | business name | [optional] 

## Example

```python
from factpulse.models.afnor_search_siret_filters_name import AFNORSearchSiretFiltersName

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSearchSiretFiltersName from a JSON string
afnor_search_siret_filters_name_instance = AFNORSearchSiretFiltersName.from_json(json)
# print the JSON string representation of the object
print(AFNORSearchSiretFiltersName.to_json())

# convert the object into a dict
afnor_search_siret_filters_name_dict = afnor_search_siret_filters_name_instance.to_dict()
# create an instance of AFNORSearchSiretFiltersName from a dict
afnor_search_siret_filters_name_from_dict = AFNORSearchSiretFiltersName.from_dict(afnor_search_siret_filters_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


