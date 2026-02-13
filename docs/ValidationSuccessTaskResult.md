# ValidationSuccessTaskResult

Successful result from task_validate_facturx_pdf.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] [default to 'SUCCESS']
**validation_result** | [**PDFValidationResultAPI**](PDFValidationResultAPI.md) |  | 

## Example

```python
from factpulse.models.validation_success_task_result import ValidationSuccessTaskResult

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationSuccessTaskResult from a JSON string
validation_success_task_result_instance = ValidationSuccessTaskResult.from_json(json)
# print the JSON string representation of the object
print(ValidationSuccessTaskResult.to_json())

# convert the object into a dict
validation_success_task_result_dict = validation_success_task_result_instance.to_dict()
# create an instance of ValidationSuccessTaskResult from a dict
validation_success_task_result_from_dict = ValidationSuccessTaskResult.from_dict(validation_success_task_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


