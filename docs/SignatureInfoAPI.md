# SignatureInfoAPI

Information about an electronic signature in a PDF.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | Signature field name in the PDF | 
**signer** | **str** |  | [optional] 
**signing_date** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**is_valid** | **bool** |  | [optional] 

## Example

```python
from factpulse.models.signature_info_api import SignatureInfoAPI

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureInfoAPI from a JSON string
signature_info_api_instance = SignatureInfoAPI.from_json(json)
# print the JSON string representation of the object
print(SignatureInfoAPI.to_json())

# convert the object into a dict
signature_info_api_dict = signature_info_api_instance.to_dict()
# create an instance of SignatureInfoAPI from a dict
signature_info_api_from_dict = SignatureInfoAPI.from_dict(signature_info_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


