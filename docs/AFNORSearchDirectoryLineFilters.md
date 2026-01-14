# AFNORSearchDirectoryLineFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressing_identifier** | [**AFNORSearchDirectoryLineFiltersAddressingIdentifier**](AFNORSearchDirectoryLineFiltersAddressingIdentifier.md) |  | [optional] 
**siren** | [**AFNORSearchSirenFiltersSiren**](AFNORSearchSirenFiltersSiren.md) |  | [optional] 
**siret** | [**AFNORSearchSiretFiltersSiret**](AFNORSearchSiretFiltersSiret.md) |  | [optional] 
**routing_identifier** | [**AFNORRoutingCodeSearchFiltersRoutingIdentifier**](AFNORRoutingCodeSearchFiltersRoutingIdentifier.md) |  | [optional] 
**addressing_suffix** | [**AFNORSearchDirectoryLineFiltersAddressingSuffix**](AFNORSearchDirectoryLineFiltersAddressingSuffix.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_search_directory_line_filters import AFNORSearchDirectoryLineFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSearchDirectoryLineFilters from a JSON string
afnor_search_directory_line_filters_instance = AFNORSearchDirectoryLineFilters.from_json(json)
# print the JSON string representation of the object
print(AFNORSearchDirectoryLineFilters.to_json())

# convert the object into a dict
afnor_search_directory_line_filters_dict = afnor_search_directory_line_filters_instance.to_dict()
# create an instance of AFNORSearchDirectoryLineFilters from a dict
afnor_search_directory_line_filters_from_dict = AFNORSearchDirectoryLineFilters.from_dict(afnor_search_directory_line_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


