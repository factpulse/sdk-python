# AFNORSearchSiretFiltersCountrySubdivision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**AFNORContainsOperator**](AFNORContainsOperator.md) |  | [optional] 
**value** | **str** | Subdivision of the country | [optional] 

## Example

```python
from factpulse.models.afnor_search_siret_filters_country_subdivision import AFNORSearchSiretFiltersCountrySubdivision

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSearchSiretFiltersCountrySubdivision from a JSON string
afnor_search_siret_filters_country_subdivision_instance = AFNORSearchSiretFiltersCountrySubdivision.from_json(json)
# print the JSON string representation of the object
print(AFNORSearchSiretFiltersCountrySubdivision.to_json())

# convert the object into a dict
afnor_search_siret_filters_country_subdivision_dict = afnor_search_siret_filters_country_subdivision_instance.to_dict()
# create an instance of AFNORSearchSiretFiltersCountrySubdivision from a dict
afnor_search_siret_filters_country_subdivision_from_dict = AFNORSearchSiretFiltersCountrySubdivision.from_dict(afnor_search_siret_filters_country_subdivision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


