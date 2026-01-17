# FactureElectroniqueRestApiSchemasCdarValidationErrorResponse

Erreur de validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Champ concerné | 
**message** | **str** | Message d&#39;erreur | 
**rule** | **str** |  | [optional] 
**severity** | **str** | Sévérité (error/warning) | [optional] [default to 'error']

## Example

```python
from factpulse.models.facture_electronique_rest_api_schemas_cdar_validation_error_response import FactureElectroniqueRestApiSchemasCdarValidationErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactureElectroniqueRestApiSchemasCdarValidationErrorResponse from a JSON string
facture_electronique_rest_api_schemas_cdar_validation_error_response_instance = FactureElectroniqueRestApiSchemasCdarValidationErrorResponse.from_json(json)
# print the JSON string representation of the object
print(FactureElectroniqueRestApiSchemasCdarValidationErrorResponse.to_json())

# convert the object into a dict
facture_electronique_rest_api_schemas_cdar_validation_error_response_dict = facture_electronique_rest_api_schemas_cdar_validation_error_response_instance.to_dict()
# create an instance of FactureElectroniqueRestApiSchemasCdarValidationErrorResponse from a dict
facture_electronique_rest_api_schemas_cdar_validation_error_response_from_dict = FactureElectroniqueRestApiSchemasCdarValidationErrorResponse.from_dict(facture_electronique_rest_api_schemas_cdar_validation_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


