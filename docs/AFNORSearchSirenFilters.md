# AFNORSearchSirenFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**siren** | [**AFNORSearchSirenFiltersSiren**](AFNORSearchSirenFiltersSiren.md) |  | [optional] 
**business_name** | [**AFNORSearchSirenFiltersBusinessName**](AFNORSearchSirenFiltersBusinessName.md) |  | [optional] 
**entity_type** | [**AFNORSearchSirenFiltersEntityType**](AFNORSearchSirenFiltersEntityType.md) |  | [optional] 
**administrative_status** | [**AFNORSearchSirenFiltersAdministrativeStatus**](AFNORSearchSirenFiltersAdministrativeStatus.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_search_siren_filters import AFNORSearchSirenFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSearchSirenFilters from a JSON string
afnor_search_siren_filters_instance = AFNORSearchSirenFilters.from_json(json)
# print the JSON string representation of the object
print(AFNORSearchSirenFilters.to_json())

# convert the object into a dict
afnor_search_siren_filters_dict = afnor_search_siren_filters_instance.to_dict()
# create an instance of AFNORSearchSirenFilters from a dict
afnor_search_siren_filters_from_dict = AFNORSearchSirenFilters.from_dict(afnor_search_siren_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


