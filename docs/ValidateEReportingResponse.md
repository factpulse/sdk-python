# ValidateEReportingResponse

Response after validating e-reporting data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** | Whether the data is valid | 
**report_id** | **str** | Report identifier | 
**flow_type** | **str** | Flux type | 
**errors** | [**List[FactureElectroniqueRestApiSchemasEreportingValidationError]**](FactureElectroniqueRestApiSchemasEreportingValidationError.md) | List of validation errors (if any) | [optional] 
**warnings** | [**List[FactureElectroniqueRestApiSchemasEreportingValidationError]**](FactureElectroniqueRestApiSchemasEreportingValidationError.md) | List of validation warnings (if any) | [optional] 
**message** | **str** | Status message | 

## Example

```python
from factpulse.models.validate_e_reporting_response import ValidateEReportingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateEReportingResponse from a JSON string
validate_e_reporting_response_instance = ValidateEReportingResponse.from_json(json)
# print the JSON string representation of the object
print(ValidateEReportingResponse.to_json())

# convert the object into a dict
validate_e_reporting_response_dict = validate_e_reporting_response_instance.to_dict()
# create an instance of ValidateEReportingResponse from a dict
validate_e_reporting_response_from_dict = ValidateEReportingResponse.from_dict(validate_e_reporting_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


