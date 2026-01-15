# AFNORSearchSiretFiltersAddressLines


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**AFNORContainsOperator**](AFNORContainsOperator.md) |  | [optional] 
**value** | **str** | address lines of the recipient structure having defined the directory line(s). | [optional] 

## Example

```python
from factpulse.models.afnor_search_siret_filters_address_lines import AFNORSearchSiretFiltersAddressLines

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSearchSiretFiltersAddressLines from a JSON string
afnor_search_siret_filters_address_lines_instance = AFNORSearchSiretFiltersAddressLines.from_json(json)
# print the JSON string representation of the object
print(AFNORSearchSiretFiltersAddressLines.to_json())

# convert the object into a dict
afnor_search_siret_filters_address_lines_dict = afnor_search_siret_filters_address_lines_instance.to_dict()
# create an instance of AFNORSearchSiretFiltersAddressLines from a dict
afnor_search_siret_filters_address_lines_from_dict = AFNORSearchSiretFiltersAddressLines.from_dict(afnor_search_siret_filters_address_lines_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


