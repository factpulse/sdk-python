# FactureEnrichieInfoOutput

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
from factpulse.models.facture_enrichie_info_output import FactureEnrichieInfoOutput

# TODO update the JSON string below
json = "{}"
# create an instance of FactureEnrichieInfoOutput from a JSON string
facture_enrichie_info_output_instance = FactureEnrichieInfoOutput.from_json(json)
# print the JSON string representation of the object
print(FactureEnrichieInfoOutput.to_json())

# convert the object into a dict
facture_enrichie_info_output_dict = facture_enrichie_info_output_instance.to_dict()
# create an instance of FactureEnrichieInfoOutput from a dict
facture_enrichie_info_output_from_dict = FactureEnrichieInfoOutput.from_dict(facture_enrichie_info_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


