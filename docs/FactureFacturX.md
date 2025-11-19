# FactureFacturX

Modèle de données pour une facture destinée à être convertie en Factur-X.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero_facture** | **str** |  | 
**date_echeance_paiement** | **str** |  | 
**date_facture** | **str** |  | [optional] 
**mode_depot** | [**ModeDepot**](ModeDepot.md) |  | 
**destinataire** | [**Destinataire**](Destinataire.md) |  | 
**fournisseur** | [**Fournisseur**](Fournisseur.md) |  | 
**cadre_de_facturation** | [**CadreDeFacturation**](CadreDeFacturation.md) |  | 
**references** | [**References**](References.md) |  | 
**montant_total** | [**MontantTotal**](MontantTotal.md) |  | 
**lignes_de_poste** | [**List[LigneDePoste]**](LigneDePoste.md) |  | [optional] 
**lignes_de_tva** | [**List[LigneDeTVA]**](LigneDeTVA.md) |  | [optional] 
**notes** | [**List[Note]**](Note.md) |  | [optional] 
**commentaire** | **str** |  | [optional] 
**id_utilisateur_courant** | **int** |  | [optional] 
**pieces_jointes_complementaires** | [**List[PieceJointeComplementaire]**](PieceJointeComplementaire.md) |  | [optional] 

## Example

```python
from factpulse.models.facture_factur_x import FactureFacturX

# TODO update the JSON string below
json = "{}"
# create an instance of FactureFacturX from a JSON string
facture_factur_x_instance = FactureFacturX.from_json(json)
# print the JSON string representation of the object
print(FactureFacturX.to_json())

# convert the object into a dict
facture_factur_x_dict = facture_factur_x_instance.to_dict()
# create an instance of FactureFacturX from a dict
facture_factur_x_from_dict = FactureFacturX.from_dict(facture_factur_x_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


