# MontantTotal

Contient tous les montants totaux de la facture.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**montant_ht_total** | [**MontantHtTotal**](MontantHtTotal.md) |  | 
**montant_tva** | [**MontantTva1**](MontantTva1.md) |  | 
**montant_ttc_total** | [**MontantTtcTotal**](MontantTtcTotal.md) |  | 
**montant_a_payer** | [**MontantAPayer**](MontantAPayer.md) |  | 
**acompte** | [**MontantTotalAcompte**](MontantTotalAcompte.md) |  | [optional] 
**montant_remise_globale_ttc** | [**MontantRemiseGlobaleTtc**](MontantRemiseGlobaleTtc.md) |  | [optional] 
**motif_remise_globale_ttc** | **str** |  | [optional] 

## Example

```python
from factpulse.models.montant_total import MontantTotal

# TODO update the JSON string below
json = "{}"
# create an instance of MontantTotal from a JSON string
montant_total_instance = MontantTotal.from_json(json)
# print the JSON string representation of the object
print(MontantTotal.to_json())

# convert the object into a dict
montant_total_dict = montant_total_instance.to_dict()
# create an instance of MontantTotal from a dict
montant_total_from_dict = MontantTotal.from_dict(montant_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


