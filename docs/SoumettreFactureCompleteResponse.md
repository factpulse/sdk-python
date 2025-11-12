# SoumettreFactureCompleteResponse

Réponse complète après soumission automatisée.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**succes** | **bool** | La facture a été soumise avec succès | 
**destination_type** | **str** | Type de destination | 
**resultat_chorus** | [**ResultatChorusPro**](ResultatChorusPro.md) |  | [optional] 
**resultat_afnor** | [**ResultatAFNOR**](ResultatAFNOR.md) |  | [optional] 
**facture_enrichie** | [**FactureEnrichieInfoOutput**](FactureEnrichieInfoOutput.md) | Données de la facture enrichie | 
**pdf_facturx** | [**PDFFacturXInfo**](PDFFacturXInfo.md) | Informations sur le PDF généré | 
**signature** | [**SignatureInfo**](SignatureInfo.md) |  | [optional] 
**pdf_base64** | **str** | PDF Factur-X généré (et signé si demandé) encodé en base64 | 
**message** | **str** | Message de retour | 

## Example

```python
from factpulse.models.soumettre_facture_complete_response import SoumettreFactureCompleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SoumettreFactureCompleteResponse from a JSON string
soumettre_facture_complete_response_instance = SoumettreFactureCompleteResponse.from_json(json)
# print the JSON string representation of the object
print(SoumettreFactureCompleteResponse.to_json())

# convert the object into a dict
soumettre_facture_complete_response_dict = soumettre_facture_complete_response_instance.to_dict()
# create an instance of SoumettreFactureCompleteResponse from a dict
soumettre_facture_complete_response_from_dict = SoumettreFactureCompleteResponse.from_dict(soumettre_facture_complete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


