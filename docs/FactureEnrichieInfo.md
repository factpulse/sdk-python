# FactureEnrichieInfo

Informations sur la facture enrichie.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero_facture** | **str** |  | 
**id_emetteur** | **int** |  | [optional] 
**id_destinataire** | **int** |  | [optional] 
**nom_emetteur** | **str** |  | 
**nom_destinataire** | **str** |  | 
**montant_ht_total** | **str** |  | 
**montant_tva** | **str** |  | 
**montant_ttc_total** | **str** |  | 

## Example

```python
from factpulse.models.facture_enrichie_info import FactureEnrichieInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FactureEnrichieInfo from a JSON string
facture_enrichie_info_instance = FactureEnrichieInfo.from_json(json)
# print the JSON string representation of the object
print(FactureEnrichieInfo.to_json())

# convert the object into a dict
facture_enrichie_info_dict = facture_enrichie_info_instance.to_dict()
# create an instance of FactureEnrichieInfo from a dict
facture_enrichie_info_from_dict = FactureEnrichieInfo.from_dict(facture_enrichie_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


