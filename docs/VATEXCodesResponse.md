# VATEXCodesResponse

Response for the VATEX codes endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codes** | [**List[VATEXCodeInfo]**](VATEXCodeInfo.md) |  | 
**count** | **int** |  | 
**source** | **str** |  | [optional] [default to 'https://docs.peppol.eu/poacc/billing/3.0/codelist/vatex/']

## Example

```python
from factpulse.models.vatex_codes_response import VATEXCodesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VATEXCodesResponse from a JSON string
vatex_codes_response_instance = VATEXCodesResponse.from_json(json)
# print the JSON string representation of the object
print(VATEXCodesResponse.to_json())

# convert the object into a dict
vatex_codes_response_dict = vatex_codes_response_instance.to_dict()
# create an instance of VATEXCodesResponse from a dict
vatex_codes_response_from_dict = VATEXCodesResponse.from_dict(vatex_codes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


