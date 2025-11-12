# StructureInfo

Informations d'une structure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_structure_cpp** | **int** | ID Chorus Pro de la structure | 
**identifiant_structure** | **str** | Identifiant (SIRET, SIREN) | 
**designation_structure** | **str** | Nom de la structure | 
**type_identifiant_structure** | **str** | Type d&#39;identifiant | 
**statut** | **str** | Statut (ACTIVE, INACTIVE) | 

## Example

```python
from factpulse.models.structure_info import StructureInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StructureInfo from a JSON string
structure_info_instance = StructureInfo.from_json(json)
# print the JSON string representation of the object
print(StructureInfo.to_json())

# convert the object into a dict
structure_info_dict = structure_info_instance.to_dict()
# create an instance of StructureInfo from a dict
structure_info_from_dict = StructureInfo.from_dict(structure_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


