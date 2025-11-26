# SoumettreFactureRequest

Soumission d'une facture Chorus Pro.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**ChorusProCredentials**](ChorusProCredentials.md) |  | [optional] 
**numero_facture** | **str** | Numéro de la facture | 
**date_facture** | **str** | Date de facture (format ISO: YYYY-MM-DD) | 
**date_echeance_paiement** | **str** |  | [optional] 
**id_structure_cpp** | **int** | ID Chorus Pro de la structure destinataire | 
**code_service** | **str** |  | [optional] 
**numero_engagement** | **str** |  | [optional] 
**montant_ht_total** | [**MontantHtTotal**](MontantHtTotal.md) |  | 
**montant_tva** | [**MontantTva**](MontantTva.md) |  | 
**montant_ttc_total** | [**MontantTtcTotal**](MontantTtcTotal.md) |  | 
**piece_jointe_principale_id** | **int** |  | [optional] 
**piece_jointe_principale_designation** | **str** |  | [optional] 
**commentaire** | **str** |  | [optional] 
**numero_bon_commande** | **str** |  | [optional] 
**numero_marche** | **str** |  | [optional] 

## Example

```python
from factpulse.models.soumettre_facture_request import SoumettreFactureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SoumettreFactureRequest from a JSON string
soumettre_facture_request_instance = SoumettreFactureRequest.from_json(json)
# print the JSON string representation of the object
print(SoumettreFactureRequest.to_json())

# convert the object into a dict
soumettre_facture_request_dict = soumettre_facture_request_instance.to_dict()
# create an instance of SoumettreFactureRequest from a dict
soumettre_facture_request_from_dict = SoumettreFactureRequest.from_dict(soumettre_facture_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


