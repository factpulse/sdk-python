# InvoicePaymentInput

Payment linked to a specific invoice (flux 10.2).  Used for B2B international invoice payments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Invoice identifier | 
**invoice_date** | **date** | Original invoice date | 
**payment_date** | **date** | Payment date | 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**amounts_by_rate** | [**List[PaymentAmountByRate]**](PaymentAmountByRate.md) | Payment amounts by VAT rate | 

## Example

```python
from factpulse.models.invoice_payment_input import InvoicePaymentInput

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicePaymentInput from a JSON string
invoice_payment_input_instance = InvoicePaymentInput.from_json(json)
# print the JSON string representation of the object
print(InvoicePaymentInput.to_json())

# convert the object into a dict
invoice_payment_input_dict = invoice_payment_input_instance.to_dict()
# create an instance of InvoicePaymentInput from a dict
invoice_payment_input_from_dict = InvoicePaymentInput.from_dict(invoice_payment_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


