# SearchStructureRequest

Search structures by criteria.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**ChorusProCredentials**](ChorusProCredentials.md) |  | [optional] 
**structure_identifier** | **str** |  | [optional] 
**structure_identifier_type** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**restrict_private_structures** | **bool** | Limit search to private structures only | [optional] [default to False]

## Example

```python
from factpulse.models.search_structure_request import SearchStructureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchStructureRequest from a JSON string
search_structure_request_instance = SearchStructureRequest.from_json(json)
# print the JSON string representation of the object
print(SearchStructureRequest.to_json())

# convert the object into a dict
search_structure_request_dict = search_structure_request_instance.to_dict()
# create an instance of SearchStructureRequest from a dict
search_structure_request_from_dict = SearchStructureRequest.from_dict(search_structure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


