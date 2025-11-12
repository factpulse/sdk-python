# ReponseSoumissionFlux

Réponse après soumission d'un flux

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **str** | Identifiant unique du flux généré par la PDP | 
**tracking_id** | **str** |  | [optional] 
**nom** | **str** | Nom du flux | 
**syntaxe_flux** | **str** | Syntaxe du flux (CII, UBL, etc.) | 
**profil_flux** | **str** |  | [optional] 
**sha256** | **str** | Hash SHA256 du fichier soumis | 
**message** | **str** | Message de confirmation | 

## Example

```python
from factpulse.models.reponse_soumission_flux import ReponseSoumissionFlux

# TODO update the JSON string below
json = "{}"
# create an instance of ReponseSoumissionFlux from a JSON string
reponse_soumission_flux_instance = ReponseSoumissionFlux.from_json(json)
# print the JSON string representation of the object
print(ReponseSoumissionFlux.to_json())

# convert the object into a dict
reponse_soumission_flux_dict = reponse_soumission_flux_instance.to_dict()
# create an instance of ReponseSoumissionFlux from a dict
reponse_soumission_flux_from_dict = ReponseSoumissionFlux.from_dict(reponse_soumission_flux_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


