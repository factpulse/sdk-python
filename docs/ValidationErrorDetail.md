# ValidationErrorDetail

Validation error detail (aligned with AFNOR AcknowledgementDetail).  Unified format for all Factur-X validation errors, compatible with AFNOR XP Z12-013 standard.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | [**ErrorLevel**](ErrorLevel.md) | Severity level: &#39;Error&#39; or &#39;Warning&#39; | [optional] 
**item** | **str** | Identifier of the concerned element (XPath, field, BR-FR rule, etc.) | 
**reason** | **str** | Error description | 
**source** | [**ErrorSource**](ErrorSource.md) |  | [optional] 
**code** | **str** |  | [optional] 

## Example

```python
from factpulse.models.validation_error_detail import ValidationErrorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationErrorDetail from a JSON string
validation_error_detail_instance = ValidationErrorDetail.from_json(json)
# print the JSON string representation of the object
print(ValidationErrorDetail.to_json())

# convert the object into a dict
validation_error_detail_dict = validation_error_detail_instance.to_dict()
# create an instance of ValidationErrorDetail from a dict
validation_error_detail_from_dict = ValidationErrorDetail.from_dict(validation_error_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


