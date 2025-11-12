# RechercherStructureResponse

Réponse de recherche de structures.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code_retour** | **int** | Code retour (0 &#x3D; succès) | 
**libelle** | **str** | Message de retour | 
**liste_structures** | [**List[StructureInfo]**](StructureInfo.md) |  | [optional] 
**total** | **int** | Nombre total de résultats | [optional] [default to 0]

## Example

```python
from factpulse.models.rechercher_structure_response import RechercherStructureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RechercherStructureResponse from a JSON string
rechercher_structure_response_instance = RechercherStructureResponse.from_json(json)
# print the JSON string representation of the object
print(RechercherStructureResponse.to_json())

# convert the object into a dict
rechercher_structure_response_dict = rechercher_structure_response_instance.to_dict()
# create an instance of RechercherStructureResponse from a dict
rechercher_structure_response_from_dict = RechercherStructureResponse.from_dict(rechercher_structure_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


