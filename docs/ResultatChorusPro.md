# ResultatChorusPro

Résultat de la soumission à Chorus Pro.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiant_facture_cpp** | **int** | ID Chorus Pro de la facture soumise | 
**numero_flux_depot** | **str** |  | [optional] 
**piece_jointe_id** | **int** |  | [optional] 

## Example

```python
from factpulse.models.resultat_chorus_pro import ResultatChorusPro

# TODO update the JSON string below
json = "{}"
# create an instance of ResultatChorusPro from a JSON string
resultat_chorus_pro_instance = ResultatChorusPro.from_json(json)
# print the JSON string representation of the object
print(ResultatChorusPro.to_json())

# convert the object into a dict
resultat_chorus_pro_dict = resultat_chorus_pro_instance.to_dict()
# create an instance of ResultatChorusPro from a dict
resultat_chorus_pro_from_dict = ResultatChorusPro.from_dict(resultat_chorus_pro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


