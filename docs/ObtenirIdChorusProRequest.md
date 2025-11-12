# ObtenirIdChorusProRequest

Obtenir l'ID Chorus Pro depuis un SIRET.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**ChorusProCredentials**](ChorusProCredentials.md) |  | [optional] 
**siret** | **str** | SIRET de la structure (14 chiffres) | 
**type_identifiant** | **str** | Type d&#39;identifiant (SIRET, SIREN, UE_HORS_FRANCE, etc.) | [optional] [default to 'SIRET']

## Example

```python
from factpulse.models.obtenir_id_chorus_pro_request import ObtenirIdChorusProRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ObtenirIdChorusProRequest from a JSON string
obtenir_id_chorus_pro_request_instance = ObtenirIdChorusProRequest.from_json(json)
# print the JSON string representation of the object
print(ObtenirIdChorusProRequest.to_json())

# convert the object into a dict
obtenir_id_chorus_pro_request_dict = obtenir_id_chorus_pro_request_instance.to_dict()
# create an instance of ObtenirIdChorusProRequest from a dict
obtenir_id_chorus_pro_request_from_dict = ObtenirIdChorusProRequest.from_dict(obtenir_id_chorus_pro_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


