# LigneDePoste

Représente une ligne de détail dans une facture.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero** | **int** |  | 
**reference** | **str** |  | [optional] 
**denomination** | **str** |  | 
**quantite** | [**Quantite**](Quantite.md) |  | 
**unite** | [**Unite**](Unite.md) |  | 
**montant_unitaire_ht** | [**MontantUnitaireHt**](MontantUnitaireHt.md) |  | 
**montant_remise_ht** | [**LigneDePosteMontantRemiseHt**](LigneDePosteMontantRemiseHt.md) |  | [optional] 
**montant_total_ligne_ht** | [**MontantTotalLigneHt**](MontantTotalLigneHt.md) |  | [optional] 
**taux_tva** | **str** |  | [optional] 
**taux_tva_manuel** | [**LigneDePosteTauxTvaManuel**](LigneDePosteTauxTvaManuel.md) |  | [optional] 
**categorie_tva** | [**CategorieTVA**](CategorieTVA.md) |  | [optional] 
**date_debut_periode** | **str** |  | [optional] 
**date_fin_periode** | **str** |  | [optional] 
**code_raison_reduction** | [**CodeRaisonReduction**](CodeRaisonReduction.md) |  | [optional] 
**raison_reduction** | **str** |  | [optional] 

## Example

```python
from factpulse.models.ligne_de_poste import LigneDePoste

# TODO update the JSON string below
json = "{}"
# create an instance of LigneDePoste from a JSON string
ligne_de_poste_instance = LigneDePoste.from_json(json)
# print the JSON string representation of the object
print(LigneDePoste.to_json())

# convert the object into a dict
ligne_de_poste_dict = ligne_de_poste_instance.to_dict()
# create an instance of LigneDePoste from a dict
ligne_de_poste_from_dict = LigneDePoste.from_dict(ligne_de_poste_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


