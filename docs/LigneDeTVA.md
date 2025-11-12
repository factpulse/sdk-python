# LigneDeTVA

Représente une ligne de totalisation par taux de TVA.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**montant_base_ht** | [**Montantbaseht**](Montantbaseht.md) |  | 
**montant_tva** | [**Montanttva**](Montanttva.md) |  | 
**taux** | **str** |  | [optional] 
**taux_manuel** | [**Tauxmanuel**](Tauxmanuel.md) |  | [optional] 
**categorie** | [**CategorieTVA**](CategorieTVA.md) |  | [optional] 

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


