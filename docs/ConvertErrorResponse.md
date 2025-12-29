# ConvertErrorResponse

Reponse erreur de conversion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] [default to 'error']
**error** | **str** | Code erreur | 
**message** | **str** | Message d&#39;erreur | 
**conversion_id** | **str** |  | [optional] 
**resume_url** | **str** |  | [optional] 

## Example

```python
from factpulse.models.convert_error_response import ConvertErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertErrorResponse from a JSON string
convert_error_response_instance = ConvertErrorResponse.from_json(json)
# print the JSON string representation of the object
print(ConvertErrorResponse.to_json())

# convert the object into a dict
convert_error_response_dict = convert_error_response_instance.to_dict()
# create an instance of ConvertErrorResponse from a dict
convert_error_response_from_dict = ConvertErrorResponse.from_dict(convert_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


