# SubmitInvoiceRequest

Submit an invoice to Chorus Pro.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**ChorusProCredentials**](ChorusProCredentials.md) |  | [optional] 
**invoice_number** | **str** | Invoice number | 
**invoice_date** | **str** | Invoice date (ISO format: YYYY-MM-DD) | 
**payment_due_date** | **str** |  | [optional] 
**structure_id** | **int** | Chorus Pro recipient structure ID | 
**service_code** | **str** |  | [optional] 
**engagement_number** | **str** |  | [optional] 
**total_net_amount** | [**SubmitNetAmount**](SubmitNetAmount.md) |  | 
**vat_amount** | [**SubmitVatAmount**](SubmitVatAmount.md) |  | 
**total_gross_amount** | [**SubmitGrossAmount**](SubmitGrossAmount.md) |  | 
**main_attachment_id** | **int** |  | [optional] 
**main_attachment_label** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**purchase_order_reference** | **str** |  | [optional] 
**contract_reference** | **str** |  | [optional] 

## Example

```python
from factpulse.models.submit_invoice_request import SubmitInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitInvoiceRequest from a JSON string
submit_invoice_request_instance = SubmitInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(SubmitInvoiceRequest.to_json())

# convert the object into a dict
submit_invoice_request_dict = submit_invoice_request_instance.to_dict()
# create an instance of SubmitInvoiceRequest from a dict
submit_invoice_request_from_dict = SubmitInvoiceRequest.from_dict(submit_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


