# RechercherStructureRequest

Recherche de structures par critères.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**ChorusProCredentials**](ChorusProCredentials.md) |  | [optional] 
**identifiant_structure** | **str** |  | [optional] 
**type_identifiant_structure** | **str** |  | [optional] 
**raison_sociale_structure** | **str** |  | [optional] 
**restreindre_structures_privees** | **bool** | Limiter la recherche aux structures privées uniquement | [optional] [default to False]

## Example

```python
from factpulse.models.rechercher_structure_request import RechercherStructureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RechercherStructureRequest from a JSON string
rechercher_structure_request_instance = RechercherStructureRequest.from_json(json)
# print the JSON string representation of the object
print(RechercherStructureRequest.to_json())

# convert the object into a dict
rechercher_structure_request_dict = rechercher_structure_request_instance.to_dict()
# create an instance of RechercherStructureRequest from a dict
rechercher_structure_request_from_dict = RechercherStructureRequest.from_dict(rechercher_structure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


