# AFNORSearchDirectoryLineFiltersAddressingSuffix


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**AFNORStrictOperator**](AFNORStrictOperator.md) |  | [optional] 
**value** | **str** | suffix of the directory line which defines an address mesh not attached to a facility | [optional] 

## Example

```python
from factpulse.models.afnor_search_directory_line_filters_addressing_suffix import AFNORSearchDirectoryLineFiltersAddressingSuffix

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSearchDirectoryLineFiltersAddressingSuffix from a JSON string
afnor_search_directory_line_filters_addressing_suffix_instance = AFNORSearchDirectoryLineFiltersAddressingSuffix.from_json(json)
# print the JSON string representation of the object
print(AFNORSearchDirectoryLineFiltersAddressingSuffix.to_json())

# convert the object into a dict
afnor_search_directory_line_filters_addressing_suffix_dict = afnor_search_directory_line_filters_addressing_suffix_instance.to_dict()
# create an instance of AFNORSearchDirectoryLineFiltersAddressingSuffix from a dict
afnor_search_directory_line_filters_addressing_suffix_from_dict = AFNORSearchDirectoryLineFiltersAddressingSuffix.from_dict(afnor_search_directory_line_filters_addressing_suffix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


