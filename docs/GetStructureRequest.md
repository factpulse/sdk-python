# GetStructureRequest

Get structure details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**FactureElectroniqueRestApiSchemasChorusProChorusProCredentials**](FactureElectroniqueRestApiSchemasChorusProChorusProCredentials.md) |  | [optional] 
**structure_id** | **int** | Chorus Pro structure ID | 
**language_code** | **str** | Language code (fr, en) | [optional] [default to 'fr']

## Example

```python
from factpulse.models.get_structure_request import GetStructureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetStructureRequest from a JSON string
get_structure_request_instance = GetStructureRequest.from_json(json)
# print the JSON string representation of the object
print(GetStructureRequest.to_json())

# convert the object into a dict
get_structure_request_dict = get_structure_request_instance.to_dict()
# create an instance of GetStructureRequest from a dict
get_structure_request_from_dict = GetStructureRequest.from_dict(get_structure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


