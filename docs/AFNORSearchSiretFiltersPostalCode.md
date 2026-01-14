# AFNORSearchSiretFiltersPostalCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**AFNORContainsOperator**](AFNORContainsOperator.md) |  | [optional] 
**value** | **str** | Service postal code | [optional] 

## Example

```python
from factpulse.models.afnor_search_siret_filters_postal_code import AFNORSearchSiretFiltersPostalCode

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSearchSiretFiltersPostalCode from a JSON string
afnor_search_siret_filters_postal_code_instance = AFNORSearchSiretFiltersPostalCode.from_json(json)
# print the JSON string representation of the object
print(AFNORSearchSiretFiltersPostalCode.to_json())

# convert the object into a dict
afnor_search_siret_filters_postal_code_dict = afnor_search_siret_filters_postal_code_instance.to_dict()
# create an instance of AFNORSearchSiretFiltersPostalCode from a dict
afnor_search_siret_filters_postal_code_from_dict = AFNORSearchSiretFiltersPostalCode.from_dict(afnor_search_siret_filters_postal_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


