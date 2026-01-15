# EReportingValidationError

Validation error detail for E-Reporting.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field path with error | 
**message** | **str** | Error message | 
**code** | **str** |  | [optional] 

## Example

```python
from factpulse.models.e_reporting_validation_error import EReportingValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of EReportingValidationError from a JSON string
e_reporting_validation_error_instance = EReportingValidationError.from_json(json)
# print the JSON string representation of the object
print(EReportingValidationError.to_json())

# convert the object into a dict
e_reporting_validation_error_dict = e_reporting_validation_error_instance.to_dict()
# create an instance of EReportingValidationError from a dict
e_reporting_validation_error_from_dict = EReportingValidationError.from_dict(e_reporting_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


