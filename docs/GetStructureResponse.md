# GetStructureResponse

Structure details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_code** | **int** |  | 
**message** | **str** |  | 
**structure_id** | **int** |  | [optional] 
**structure_identifier** | **str** |  | [optional] 
**structure_label** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**vat_number** | **str** |  | [optional] 
**structure_email** | **str** |  | [optional] 
**parameters** | [**StructureParameters**](StructureParameters.md) |  | [optional] 

## Example

```python
from factpulse.models.get_structure_response import GetStructureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStructureResponse from a JSON string
get_structure_response_instance = GetStructureResponse.from_json(json)
# print the JSON string representation of the object
print(GetStructureResponse.to_json())

# convert the object into a dict
get_structure_response_dict = get_structure_response_instance.to_dict()
# create an instance of GetStructureResponse from a dict
get_structure_response_from_dict = GetStructureResponse.from_dict(get_structure_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


