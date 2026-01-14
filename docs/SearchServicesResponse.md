# SearchServicesResponse

Structure services list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_code** | **int** | Return code (0 &#x3D; success) | 
**message** | **str** | Response message | 
**services** | [**List[StructureService]**](StructureService.md) | List of services | [optional] 
**total** | **int** | Number of services | [optional] [default to 0]

## Example

```python
from factpulse.models.search_services_response import SearchServicesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchServicesResponse from a JSON string
search_services_response_instance = SearchServicesResponse.from_json(json)
# print the JSON string representation of the object
print(SearchServicesResponse.to_json())

# convert the object into a dict
search_services_response_dict = search_services_response_instance.to_dict()
# create an instance of SearchServicesResponse from a dict
search_services_response_from_dict = SearchServicesResponse.from_dict(search_services_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


