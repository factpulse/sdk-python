# ValidationInfo

Informations sur la validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | **str** | Profil Factur-X utilise | 
**schematron_rules_passed** | **int** | Regles passees | 
**schematron_rules_total** | **int** | Total regles | 
**pdfa_compliant** | **bool** | PDF/A-3 conforme | [optional] [default to True]
**xml_embedded** | **bool** | XML embarque dans PDF | [optional] [default to True]
**errors** | [**List[FactureElectroniqueRestApiSchemasConvertValidationError]**](FactureElectroniqueRestApiSchemasConvertValidationError.md) |  | [optional] 

## Example

```python
from factpulse.models.validation_info import ValidationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationInfo from a JSON string
validation_info_instance = ValidationInfo.from_json(json)
# print the JSON string representation of the object
print(ValidationInfo.to_json())

# convert the object into a dict
validation_info_dict = validation_info_instance.to_dict()
# create an instance of ValidationInfo from a dict
validation_info_from_dict = ValidationInfo.from_dict(validation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


