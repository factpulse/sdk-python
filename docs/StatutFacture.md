# StatutFacture

Statut d'une facture Chorus Pro.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code statut (SOUMISE, VALIDEE, REJETEE, SUSPENDUE, MANDATEE, MISE_EN_PAIEMENT, etc.) | 
**libelle** | **str** | Libellé du statut | 
**var_date** | **str** |  | [optional] 

## Example

```python
from factpulse.models.statut_facture import StatutFacture

# TODO update the JSON string below
json = "{}"
# create an instance of StatutFacture from a JSON string
statut_facture_instance = StatutFacture.from_json(json)
# print the JSON string representation of the object
print(StatutFacture.to_json())

# convert the object into a dict
statut_facture_dict = statut_facture_instance.to_dict()
# create an instance of StatutFacture from a dict
statut_facture_from_dict = StatutFacture.from_dict(statut_facture_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


