# ObtenirIdChorusProResponse

ID Chorus Pro trouvé.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_structure_cpp** | **int** | ID Chorus Pro (0 si non trouvé) | 
**identifiant_structure** | **str** | SIRET/SIREN recherché | 
**designation_structure** | **str** |  | [optional] 
**message** | **str** | Message de retour | 

## Example

```python
from factpulse.models.obtenir_id_chorus_pro_response import ObtenirIdChorusProResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ObtenirIdChorusProResponse from a JSON string
obtenir_id_chorus_pro_response_instance = ObtenirIdChorusProResponse.from_json(json)
# print the JSON string representation of the object
print(ObtenirIdChorusProResponse.to_json())

# convert the object into a dict
obtenir_id_chorus_pro_response_dict = obtenir_id_chorus_pro_response_instance.to_dict()
# create an instance of ObtenirIdChorusProResponse from a dict
obtenir_id_chorus_pro_response_from_dict = ObtenirIdChorusProResponse.from_dict(obtenir_id_chorus_pro_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


