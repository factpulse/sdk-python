# FactureElectroniqueRestApiSchemasEreportingValidationError

Validation error detail.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field path with error | 
**message** | **str** | Error message | 
**code** | **str** |  | [optional] 

## Example

```python
from factpulse.models.facture_electronique_rest_api_schemas_ereporting_validation_error import FactureElectroniqueRestApiSchemasEreportingValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of FactureElectroniqueRestApiSchemasEreportingValidationError from a JSON string
facture_electronique_rest_api_schemas_ereporting_validation_error_instance = FactureElectroniqueRestApiSchemasEreportingValidationError.from_json(json)
# print the JSON string representation of the object
print(FactureElectroniqueRestApiSchemasEreportingValidationError.to_json())

# convert the object into a dict
facture_electronique_rest_api_schemas_ereporting_validation_error_dict = facture_electronique_rest_api_schemas_ereporting_validation_error_instance.to_dict()
# create an instance of FactureElectroniqueRestApiSchemasEreportingValidationError from a dict
facture_electronique_rest_api_schemas_ereporting_validation_error_from_dict = FactureElectroniqueRestApiSchemasEreportingValidationError.from_dict(facture_electronique_rest_api_schemas_ereporting_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


