# AFNORSearchDirectoryLineFiltersAddressingIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**AFNORContainsOperator**](AFNORContainsOperator.md) |  | [optional] 
**value** | **str** | Addressing identifier of the directory line. | [optional] 

## Example

```python
from factpulse.models.afnor_search_directory_line_filters_addressing_identifier import AFNORSearchDirectoryLineFiltersAddressingIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORSearchDirectoryLineFiltersAddressingIdentifier from a JSON string
afnor_search_directory_line_filters_addressing_identifier_instance = AFNORSearchDirectoryLineFiltersAddressingIdentifier.from_json(json)
# print the JSON string representation of the object
print(AFNORSearchDirectoryLineFiltersAddressingIdentifier.to_json())

# convert the object into a dict
afnor_search_directory_line_filters_addressing_identifier_dict = afnor_search_directory_line_filters_addressing_identifier_instance.to_dict()
# create an instance of AFNORSearchDirectoryLineFiltersAddressingIdentifier from a dict
afnor_search_directory_line_filters_addressing_identifier_from_dict = AFNORSearchDirectoryLineFiltersAddressingIdentifier.from_dict(afnor_search_directory_line_filters_addressing_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


