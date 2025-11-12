# ConsulterStructureResponse

Détails d'une structure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code_retour** | **int** |  | 
**libelle** | **str** |  | 
**id_structure_cpp** | **int** |  | [optional] 
**identifiant_structure** | **str** |  | [optional] 
**libelle_structure** | **str** |  | [optional] 
**raison_sociale_structure** | **str** |  | [optional] 
**numero_tva** | **str** |  | [optional] 
**email_structure** | **str** |  | [optional] 
**parametres** | [**ParametresStructure**](ParametresStructure.md) |  | [optional] 

## Example

```python
from factpulse.models.consulter_structure_response import ConsulterStructureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConsulterStructureResponse from a JSON string
consulter_structure_response_instance = ConsulterStructureResponse.from_json(json)
# print the JSON string representation of the object
print(ConsulterStructureResponse.to_json())

# convert the object into a dict
consulter_structure_response_dict = consulter_structure_response_instance.to_dict()
# create an instance of ConsulterStructureResponse from a dict
consulter_structure_response_from_dict = ConsulterStructureResponse.from_dict(consulter_structure_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


