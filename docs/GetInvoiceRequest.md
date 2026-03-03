# GetInvoiceRequest

Get an invoice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**ChorusProCredentials**](ChorusProCredentials.md) |  | [optional] 
**chorus_invoice_id** | **int** | Chorus Pro invoice ID | 

## Example

```python
from factpulse.models.get_invoice_request import GetInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoiceRequest from a JSON string
get_invoice_request_instance = GetInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(GetInvoiceRequest.to_json())

# convert the object into a dict
get_invoice_request_dict = get_invoice_request_instance.to_dict()
# create an instance of GetInvoiceRequest from a dict
get_invoice_request_from_dict = GetInvoiceRequest.from_dict(get_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


