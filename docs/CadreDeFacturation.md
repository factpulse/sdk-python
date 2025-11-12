# CadreDeFacturation

Définit le cadre de facturation (ex: A1 pour une facture fournisseur).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code_cadre_facturation** | [**CodeCadreFacturation**](CodeCadreFacturation.md) |  | 
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


