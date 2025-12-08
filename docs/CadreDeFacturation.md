# CadreDeFacturation

Définit le cadre de facturation.  - code_cadre_facturation: Code Chorus Pro (A1, A2, A9, A12) - utilisé pour B2G - nature_operation: Nature de l'opération (B1, S1, M1, etc.) - prioritaire pour Factur-X  Si nature_operation est fourni, il sera utilisé directement dans le XML Factur-X (BT-23). Sinon, le code sera déduit de code_cadre_facturation via un mapping automatique.  Exemple:     >>> cadre = CadreDeFacturation(     ...     code_cadre_facturation=CodeCadreFacturation.A1_FACTURE_FOURNISSEUR,     ...     nature_operation=NatureOperation.BIENS  # Force B1 au lieu de S1     ... )

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code_cadre_facturation** | [**CodeCadreFacturation**](CodeCadreFacturation.md) |  | 
**nature_operation** | [**NatureOperation**](NatureOperation.md) |  | [optional] 
**code_service_valideur** | **str** |  | [optional] 
**code_structure_valideur** | **str** |  | [optional] 

## Example

```python
from factpulse.models.cadre_de_facturation import CadreDeFacturation

# TODO update the JSON string below
json = "{}"
# create an instance of CadreDeFacturation from a JSON string
cadre_de_facturation_instance = CadreDeFacturation.from_json(json)
# print the JSON string representation of the object
print(CadreDeFacturation.to_json())

# convert the object into a dict
cadre_de_facturation_dict = cadre_de_facturation_instance.to_dict()
# create an instance of CadreDeFacturation from a dict
cadre_de_facturation_from_dict = CadreDeFacturation.from_dict(cadre_de_facturation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


