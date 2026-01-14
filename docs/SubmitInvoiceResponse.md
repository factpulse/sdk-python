# SubmitInvoiceResponse

Response after invoice submission.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_code** | **int** | Return code (0 &#x3D; success) | 
**message** | **str** | Return message | 
**chorus_invoice_id** | **int** |  | [optional] 
**deposit_flow_number** | **str** |  | [optional] 

## Example

```python
from factpulse.models.submit_invoice_response import SubmitInvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitInvoiceResponse from a JSON string
submit_invoice_response_instance = SubmitInvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(SubmitInvoiceResponse.to_json())

# convert the object into a dict
submit_invoice_response_dict = submit_invoice_response_instance.to_dict()
# create an instance of SubmitInvoiceResponse from a dict
submit_invoice_response_from_dict = SubmitInvoiceResponse.from_dict(submit_invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


