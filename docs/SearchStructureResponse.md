# SearchStructureResponse

Structure search response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_code** | **int** | Return code (0 &#x3D; success) | 
**message** | **str** | Return message | 
**structures** | [**List[StructureInfo]**](StructureInfo.md) |  | [optional] 
**total** | **int** | Total number of results | [optional] [default to 0]

## Example

```python
from factpulse.models.search_structure_response import SearchStructureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchStructureResponse from a JSON string
search_structure_response_instance = SearchStructureResponse.from_json(json)
# print the JSON string representation of the object
print(SearchStructureResponse.to_json())

# convert the object into a dict
search_structure_response_dict = search_structure_response_instance.to_dict()
# create an instance of SearchStructureResponse from a dict
search_structure_response_from_dict = SearchStructureResponse.from_dict(search_structure_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


