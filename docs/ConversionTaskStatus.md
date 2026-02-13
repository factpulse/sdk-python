# ConversionTaskStatus

Typed task status for document conversion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | 
**status** | [**CeleryStatus**](CeleryStatus.md) |  | 
**result** | [**ConversionTaskStatusResult**](ConversionTaskStatusResult.md) |  | [optional] 

## Example

```python
from factpulse.models.conversion_task_status import ConversionTaskStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionTaskStatus from a JSON string
conversion_task_status_instance = ConversionTaskStatus.from_json(json)
# print the JSON string representation of the object
print(ConversionTaskStatus.to_json())

# convert the object into a dict
conversion_task_status_dict = conversion_task_status_instance.to_dict()
# create an instance of ConversionTaskStatus from a dict
conversion_task_status_from_dict = ConversionTaskStatus.from_dict(conversion_task_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


