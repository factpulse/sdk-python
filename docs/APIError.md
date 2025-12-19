# APIError

Standardized API error (aligned with AFNOR Error schema).  Unified format for all HTTP error responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** | Alphanumeric code precisely identifying the error | 
**error_message** | **str** | Message describing the error (not intended for end user) | 
**details** | [**List[ValidationErrorDetail]**](ValidationErrorDetail.md) |  | [optional] 

## Example

```python
from factpulse.models.api_error import APIError

# TODO update the JSON string below
json = "{}"
# create an instance of APIError from a JSON string
api_error_instance = APIError.from_json(json)
# print the JSON string representation of the object
print(APIError.to_json())

# convert the object into a dict
api_error_dict = api_error_instance.to_dict()
# create an instance of APIError from a dict
api_error_from_dict = APIError.from_dict(api_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


