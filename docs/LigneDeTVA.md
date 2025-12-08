# LigneDeTVA

Représente une ligne de totalisation par taux de TVA.  Pour les exonérations (catégories E, AE, K, G, O), les champs `motif_exoneration` et `code_vatex` sont requis selon EN16931.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**montant_base_ht** | [**MontantBaseHt**](MontantBaseHt.md) |  | 
**montant_tva** | [**MontantTvaLigne**](MontantTvaLigne.md) |  | 
**taux** | **str** |  | [optional] 
**taux_manuel** | [**Tauxmanuel**](Tauxmanuel.md) |  | [optional] 
**categorie** | [**CategorieTVA**](CategorieTVA.md) |  | [optional] 
**motif_exoneration** | **str** |  | [optional] 
**code_vatex** | **str** |  | [optional] 

## Example

```python
from factpulse.models.ligne_de_tva import LigneDeTVA

# TODO update the JSON string below
json = "{}"
# create an instance of LigneDeTVA from a JSON string
ligne_de_tva_instance = LigneDeTVA.from_json(json)
# print the JSON string representation of the object
print(LigneDeTVA.to_json())

# convert the object into a dict
ligne_de_tva_dict = ligne_de_tva_instance.to_dict()
# create an instance of LigneDeTVA from a dict
ligne_de_tva_from_dict = LigneDeTVA.from_dict(ligne_de_tva_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


