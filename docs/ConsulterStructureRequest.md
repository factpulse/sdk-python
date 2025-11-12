# ConsulterStructureRequest

Consulter les détails d'une structure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**ChorusProCredentials**](ChorusProCredentials.md) |  | [optional] 
**id_structure_cpp** | **int** | ID Chorus Pro de la structure | 
**code_langue** | **str** | Code langue (fr, en) | [optional] [default to 'fr']

## Example

```python
from factpulse.models.consulter_structure_request import ConsulterStructureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConsulterStructureRequest from a JSON string
consulter_structure_request_instance = ConsulterStructureRequest.from_json(json)
# print the JSON string representation of the object
print(ConsulterStructureRequest.to_json())

# convert the object into a dict
consulter_structure_request_dict = consulter_structure_request_instance.to_dict()
# create an instance of ConsulterStructureRequest from a dict
consulter_structure_request_from_dict = ConsulterStructureRequest.from_dict(consulter_structure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


