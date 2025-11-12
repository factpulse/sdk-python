# FactureEnrichieInfoInput

Informations sur la facture enrichie.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero_facture** | **str** |  | 
**id_emetteur** | **int** |  | [optional] 
**id_destinataire** | **int** |  | [optional] 
**nom_emetteur** | **str** |  | 
**nom_destinataire** | **str** |  | 
**montant_ht_total** | [**MontantHtTotal**](MontantHtTotal.md) |  | 
**montant_tva** | [**MontantTva**](MontantTva.md) |  | 
**montant_ttc_total** | [**MontantTtcTotal**](MontantTtcTotal.md) |  | 

## Example

```python
from factpulse.models.facture_enrichie_info_input import FactureEnrichieInfoInput

# TODO update the JSON string below
json = "{}"
# create an instance of FactureEnrichieInfoInput from a JSON string
facture_enrichie_info_input_instance = FactureEnrichieInfoInput.from_json(json)
# print the JSON string representation of the object
print(FactureEnrichieInfoInput.to_json())

# convert the object into a dict
facture_enrichie_info_input_dict = facture_enrichie_info_input_instance.to_dict()
# create an instance of FactureEnrichieInfoInput from a dict
facture_enrichie_info_input_from_dict = FactureEnrichieInfoInput.from_dict(facture_enrichie_info_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


