# ServiceStructure

Service d'une structure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_service** | **int** | ID du service | 
**code_service** | **str** | Code du service | 
**libelle_service** | **str** | Libellé du service | 
**est_actif** | **bool** | Service actif | 

## Example

```python
from factpulse.models.service_structure import ServiceStructure

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStructure from a JSON string
service_structure_instance = ServiceStructure.from_json(json)
# print the JSON string representation of the object
print(ServiceStructure.to_json())

# convert the object into a dict
service_structure_dict = service_structure_instance.to_dict()
# create an instance of ServiceStructure from a dict
service_structure_from_dict = ServiceStructure.from_dict(service_structure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


