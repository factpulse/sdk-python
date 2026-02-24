# FactureElectroniqueRestApiSchemasValidationValidationErrorResponse

Response for validation errors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **List[str]** | List of detected validation errors. | 

## Example

```python
from factpulse.models.facture_electronique_rest_api_schemas_validation_validation_error_response import FactureElectroniqueRestApiSchemasValidationValidationErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FactureElectroniqueRestApiSchemasValidationValidationErrorResponse from a JSON string
facture_electronique_rest_api_schemas_validation_validation_error_response_instance = FactureElectroniqueRestApiSchemasValidationValidationErrorResponse.from_json(json)
# print the JSON string representation of the object
print(FactureElectroniqueRestApiSchemasValidationValidationErrorResponse.to_json())

# convert the object into a dict
facture_electronique_rest_api_schemas_validation_validation_error_response_dict = facture_electronique_rest_api_schemas_validation_validation_error_response_instance.to_dict()
# create an instance of FactureElectroniqueRestApiSchemasValidationValidationErrorResponse from a dict
facture_electronique_rest_api_schemas_validation_validation_error_response_from_dict = FactureElectroniqueRestApiSchemasValidationValidationErrorResponse.from_dict(facture_electronique_rest_api_schemas_validation_validation_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


