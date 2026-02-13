# SignatureSuccessResult

Successful result from task_sign_pdf_from_bytes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] [default to 'SUCCESS']
**content_b64** | **str** |  | 
**filename** | **str** |  | 
**size_bytes** | **int** |  | 
**is_signed** | **bool** |  | 
**signature_count** | **int** |  | 
**signer_cn** | **str** |  | 
**signing_date** | **str** |  | 
**validation_details** | **Dict[str, object]** |  | 

## Example

```python
from factpulse.models.signature_success_result import SignatureSuccessResult

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureSuccessResult from a JSON string
signature_success_result_instance = SignatureSuccessResult.from_json(json)
# print the JSON string representation of the object
print(SignatureSuccessResult.to_json())

# convert the object into a dict
signature_success_result_dict = signature_success_result_instance.to_dict()
# create an instance of SignatureSuccessResult from a dict
signature_success_result_from_dict = SignatureSuccessResult.from_dict(signature_success_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


