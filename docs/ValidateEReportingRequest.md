# ValidateEReportingRequest

Request to validate e-reporting data without submitting.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateEReportingRequest**](CreateEReportingRequest.md) | E-Reporting data to validate | 

## Example

```python
from factpulse.models.validate_e_reporting_request import ValidateEReportingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateEReportingRequest from a JSON string
validate_e_reporting_request_instance = ValidateEReportingRequest.from_json(json)
# print the JSON string representation of the object
print(ValidateEReportingRequest.to_json())

# convert the object into a dict
validate_e_reporting_request_dict = validate_e_reporting_request_instance.to_dict()
# create an instance of ValidateEReportingRequest from a dict
validate_e_reporting_request_from_dict = ValidateEReportingRequest.from_dict(validate_e_reporting_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


