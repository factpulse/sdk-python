# ValidationTaskStatusResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] [default to 'ERROR']
**validation_result** | [**PDFValidationResultAPI**](PDFValidationResultAPI.md) |  | 
**error_code** | **str** |  | 
**error_message** | **str** |  | 
**details** | [**List[AFNORErrorDetail]**](AFNORErrorDetail.md) |  | [optional] 
**traceback** | **str** |  | [optional] 

## Example

```python
from factpulse.models.validation_task_status_result import ValidationTaskStatusResult

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationTaskStatusResult from a JSON string
validation_task_status_result_instance = ValidationTaskStatusResult.from_json(json)
# print the JSON string representation of the object
print(ValidationTaskStatusResult.to_json())

# convert the object into a dict
validation_task_status_result_dict = validation_task_status_result_instance.to_dict()
# create an instance of ValidationTaskStatusResult from a dict
validation_task_status_result_from_dict = ValidationTaskStatusResult.from_dict(validation_task_status_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


