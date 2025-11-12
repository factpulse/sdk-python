# SoumettreFactureResponse

Réponse après soumission de facture.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code_retour** | **int** | Code retour (0 &#x3D; succès) | 
**libelle** | **str** | Message de retour | 
**identifiant_facture_cpp** | **int** |  | [optional] 
**numero_flux_depot** | **str** |  | [optional] 

## Example

```python
from factpulse.models.soumettre_facture_response import SoumettreFactureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SoumettreFactureResponse from a JSON string
soumettre_facture_response_instance = SoumettreFactureResponse.from_json(json)
# print the JSON string representation of the object
print(SoumettreFactureResponse.to_json())

# convert the object into a dict
soumettre_facture_response_dict = soumettre_facture_response_instance.to_dict()
# create an instance of SoumettreFactureResponse from a dict
soumettre_facture_response_from_dict = SoumettreFactureResponse.from_dict(soumettre_facture_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


