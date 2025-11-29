# FactureEntrante

Facture reçue d'un fournisseur via PDP/PA.  Ce modèle contient les métadonnées essentielles extraites des factures entrantes, quel que soit leur format source (CII, UBL, Factur-X).  Les montants sont en Decimal en Python mais seront sérialisés en string dans le JSON pour préserver la précision monétaire.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **str** |  | [optional] 
**format_source** | [**FormatFacture**](FormatFacture.md) | Format source de la facture | 
**ref_fournisseur** | **str** | Numéro de facture émis par le fournisseur (BT-1) | 
**type_document** | [**TypeDocument**](TypeDocument.md) | Type de document (BT-3) | [optional] 
**fournisseur** | [**FournisseurEntrant**](FournisseurEntrant.md) | Émetteur de la facture (SellerTradeParty) | 
**site_facturation_nom** | **str** | Nom du destinataire / votre entreprise (BT-44) | 
**site_facturation_siret** | **str** |  | [optional] 
**date_de_piece** | **str** | Date de la facture (BT-2) - YYYY-MM-DD | 
**date_reglement** | **str** |  | [optional] 
**devise** | **str** | Code devise ISO (BT-5) | [optional] [default to 'EUR']
**montant_ht** | **str** | Montant HT total (BT-109) | 
**montant_tva** | **str** | Montant TVA total (BT-110) | 
**montant_ttc** | **str** | Montant TTC total (BT-112) | 
**numero_bon_commande** | **str** |  | [optional] 
**reference_contrat** | **str** |  | [optional] 
**objet_facture** | **str** |  | [optional] 

## Example

```python
from factpulse.models.facture_entrante import FactureEntrante

# TODO update the JSON string below
json = "{}"
# create an instance of FactureEntrante from a JSON string
facture_entrante_instance = FactureEntrante.from_json(json)
# print the JSON string representation of the object
print(FactureEntrante.to_json())

# convert the object into a dict
facture_entrante_dict = facture_entrante_instance.to_dict()
# create an instance of FactureEntrante from a dict
facture_entrante_from_dict = FactureEntrante.from_dict(facture_entrante_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


