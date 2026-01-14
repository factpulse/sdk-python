# FactureElectroniqueRestApiSchemasConvertValidationError

Erreur de validation Schematron avec suggestion de correction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule** | **str** | Code de la regle (BR-XX, BR-FR-XX) | 
**bt_code** | **str** |  | [optional] 
**severity** | **str** | Gravite: error, warning | 
**message** | **str** | Message d&#39;erreur | 
**suggested_value** | **str** |  | [optional] 
**suggested_field** | **str** |  | [optional] 
**explanation** | **str** |  | [optional] 
**confidence** | **float** |  | [optional] 

## Example

```python
from factpulse.models.facture_electronique_rest_api_schemas_convert_validation_error import FactureElectroniqueRestApiSchemasConvertValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of FactureElectroniqueRestApiSchemasConvertValidationError from a JSON string
facture_electronique_rest_api_schemas_convert_validation_error_instance = FactureElectroniqueRestApiSchemasConvertValidationError.from_json(json)
# print the JSON string representation of the object
print(FactureElectroniqueRestApiSchemasConvertValidationError.to_json())

# convert the object into a dict
facture_electronique_rest_api_schemas_convert_validation_error_dict = facture_electronique_rest_api_schemas_convert_validation_error_instance.to_dict()
# create an instance of FactureElectroniqueRestApiSchemasConvertValidationError from a dict
facture_electronique_rest_api_schemas_convert_validation_error_from_dict = FactureElectroniqueRestApiSchemasConvertValidationError.from_dict(facture_electronique_rest_api_schemas_convert_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


