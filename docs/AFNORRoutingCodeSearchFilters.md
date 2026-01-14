# AFNORRoutingCodeSearchFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routing_identifier** | [**AFNORRoutingCodeSearchFiltersRoutingIdentifier**](AFNORRoutingCodeSearchFiltersRoutingIdentifier.md) |  | [optional] 
**siret** | [**AFNORSearchSiretFiltersSiret**](AFNORSearchSiretFiltersSiret.md) |  | [optional] 
**routing_code_name** | [**AFNORRoutingCodeSearchFiltersRoutingCodeName**](AFNORRoutingCodeSearchFiltersRoutingCodeName.md) |  | [optional] 
**administrative_status** | [**AFNORRoutingCodeSearchFiltersAdministrativeStatus**](AFNORRoutingCodeSearchFiltersAdministrativeStatus.md) |  | [optional] 
**address_lines** | [**AFNORSearchSiretFiltersAddressLines**](AFNORSearchSiretFiltersAddressLines.md) |  | [optional] 
**postal_code** | [**AFNORSearchSiretFiltersPostalCode**](AFNORSearchSiretFiltersPostalCode.md) |  | [optional] 
**locality** | [**AFNORSearchSiretFiltersLocality**](AFNORSearchSiretFiltersLocality.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_routing_code_search_filters import AFNORRoutingCodeSearchFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORRoutingCodeSearchFilters from a JSON string
afnor_routing_code_search_filters_instance = AFNORRoutingCodeSearchFilters.from_json(json)
# print the JSON string representation of the object
print(AFNORRoutingCodeSearchFilters.to_json())

# convert the object into a dict
afnor_routing_code_search_filters_dict = afnor_routing_code_search_filters_instance.to_dict()
# create an instance of AFNORRoutingCodeSearchFilters from a dict
afnor_routing_code_search_filters_from_dict = AFNORRoutingCodeSearchFilters.from_dict(afnor_routing_code_search_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


