# AFNORSearchSiretFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**siret** | [**AFNORSearchSiretFiltersSiret**](AFNORSearchSiretFiltersSiret.md) |  | [optional] 
**siren** | [**AFNORSearchSirenFiltersSiren**](AFNORSearchSirenFiltersSiren.md) |  | [optional] 
**facility_type** | [**AFNORSearchSiretFiltersFacilityType**](AFNORSearchSiretFiltersFacilityType.md) |  | [optional] 
**name** | [**AFNORSearchSiretFiltersName**](AFNORSearchSiretFiltersName.md) |  | [optional] 
**address_lines** | [**AFNORSearchSiretFiltersAddressLines**](AFNORSearchSiretFiltersAddressLines.md) |  | [optional] 
**postal_code** | [**AFNORSearchSiretFiltersPostalCode**](AFNORSearchSiretFiltersPostalCode.md) |  | [optional] 
**country_subdivision** | [**AFNORSearchSiretFiltersCountrySubdivision**](AFNORSearchSiretFiltersCountrySubdivision.md) |  | [optional] 
**locality** | [**AFNORSearchSiretFiltersLocality**](AFNORSearchSiretFiltersLocality.md) |  | [optional] 
**administrative_status** | [**AFNORSearchSiretFiltersAdministrativeStatus**](AFNORSearchSiretFiltersAdministrativeStatus.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_search_siret_filters import AFNORSearchSiretFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSearchSiretFilters from a JSON string
afnor_search_siret_filters_instance = AFNORSearchSiretFilters.from_json(json)
# print the JSON string representation of the object
print(AFNORSearchSiretFilters.to_json())

# convert the object into a dict
afnor_search_siret_filters_dict = afnor_search_siret_filters_instance.to_dict()
# create an instance of AFNORSearchSiretFilters from a dict
afnor_search_siret_filters_from_dict = AFNORSearchSiretFilters.from_dict(afnor_search_siret_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


