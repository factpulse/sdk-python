# ParametresStructure

Paramètres obligatoires d'une structure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code_service_doit_etre_renseigne** | **bool** | Le code service est obligatoire | [optional] [default to False]
**numero_ej_doit_etre_renseigne** | **bool** | Le numéro d&#39;engagement est obligatoire | [optional] [default to False]
**gestion_numero_ej_ou_code_service** | **bool** | Gestion EJ ou code service activée | [optional] [default to False]

## Example

```python
from factpulse.models.parametres_structure import ParametresStructure

# TODO update the JSON string below
json = "{}"
# create an instance of ParametresStructure from a JSON string
parametres_structure_instance = ParametresStructure.from_json(json)
# print the JSON string representation of the object
print(ParametresStructure.to_json())

# convert the object into a dict
parametres_structure_dict = parametres_structure_instance.to_dict()
# create an instance of ParametresStructure from a dict
parametres_structure_from_dict = ParametresStructure.from_dict(parametres_structure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


