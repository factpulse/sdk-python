# AFNORSearchSiretFiltersAdministrativeStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**AFNORStrictOperator**](AFNORStrictOperator.md) |  | [optional] 
**value** | [**AFNORFacilityAdministrativeStatus**](AFNORFacilityAdministrativeStatus.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_search_siret_filters_administrative_status import AFNORSearchSiretFiltersAdministrativeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSearchSiretFiltersAdministrativeStatus from a JSON string
afnor_search_siret_filters_administrative_status_instance = AFNORSearchSiretFiltersAdministrativeStatus.from_json(json)
# print the JSON string representation of the object
print(AFNORSearchSiretFiltersAdministrativeStatus.to_json())

# convert the object into a dict
afnor_search_siret_filters_administrative_status_dict = afnor_search_siret_filters_administrative_status_instance.to_dict()
# create an instance of AFNORSearchSiretFiltersAdministrativeStatus from a dict
afnor_search_siret_filters_administrative_status_from_dict = AFNORSearchSiretFiltersAdministrativeStatus.from_dict(afnor_search_siret_filters_administrative_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


