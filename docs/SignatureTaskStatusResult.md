# SignatureTaskStatusResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] [default to 'ERROR']
**content_b64** | **str** |  | 
**filename** | **str** |  | 
**size_bytes** | **int** |  | 
**is_signed** | **bool** |  | 
**signature_count** | **int** |  | 
**signer_cn** | **str** |  | 
**signing_date** | **str** |  | 
**validation_details** | **Dict[str, object]** |  | 
**error_code** | **str** |  | 
**error_message** | **str** |  | 
**details** | [**List[AFNORErrorDetail]**](AFNORErrorDetail.md) |  | [optional] 
**traceback** | **str** |  | [optional] 

## Example

```python
from factpulse.models.signature_task_status_result import SignatureTaskStatusResult

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureTaskStatusResult from a JSON string
signature_task_status_result_instance = SignatureTaskStatusResult.from_json(json)
# print the JSON string representation of the object
print(SignatureTaskStatusResult.to_json())

# convert the object into a dict
signature_task_status_result_dict = signature_task_status_result_instance.to_dict()
# create an instance of SignatureTaskStatusResult from a dict
signature_task_status_result_from_dict = SignatureTaskStatusResult.from_dict(signature_task_status_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


