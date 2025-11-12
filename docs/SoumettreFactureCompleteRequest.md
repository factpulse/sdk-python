# SoumettreFactureCompleteRequest

Requête pour soumettre une facture complète (génération + soumission).  Workflow : 1. Auto-enrichissement (optionnel) 2. Génération PDF Factur-X 3. Signature (optionnelle) 4. Soumission vers la destination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**donnees_facture** | [**DonneesFactureSimplifiees**](DonneesFactureSimplifiees.md) | Données de la facture au format simplifié (voir exemples) | 
**pdf_source** | **str** | PDF source encodé en base64 (sera transformé en Factur-X) | 
**destination** | [**Destination**](Destination.md) |  | 
**signature** | [**ParametresSignature**](ParametresSignature.md) |  | [optional] 
**options** | [**OptionsProcessing**](OptionsProcessing.md) | Options de traitement | [optional] 

## Example

```python
from factpulse.models.soumettre_facture_complete_request import SoumettreFactureCompleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SoumettreFactureCompleteRequest from a JSON string
soumettre_facture_complete_request_instance = SoumettreFactureCompleteRequest.from_json(json)
# print the JSON string representation of the object
print(SoumettreFactureCompleteRequest.to_json())

# convert the object into a dict
soumettre_facture_complete_request_dict = soumettre_facture_complete_request_instance.to_dict()
# create an instance of SoumettreFactureCompleteRequest from a dict
soumettre_facture_complete_request_from_dict = SoumettreFactureCompleteRequest.from_dict(soumettre_facture_complete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


