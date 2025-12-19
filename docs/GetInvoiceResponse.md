# GetInvoiceResponse

Invoice details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_code** | **int** |  | 
**message** | **str** |  | 
**chorus_invoice_id** | **int** |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**invoice_date** | **str** |  | [optional] 
**total_gross_amount** | **str** |  | [optional] 
**current_status** | [**InvoiceStatus**](InvoiceStatus.md) |  | [optional] 
**recipient_structure_id** | **int** |  | [optional] 
**recipient_structure_name** | **str** |  | [optional] 

## Example

```python
from factpulse.models.get_invoice_response import GetInvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoiceResponse from a JSON string
get_invoice_response_instance = GetInvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(GetInvoiceResponse.to_json())

# convert the object into a dict
get_invoice_response_dict = get_invoice_response_instance.to_dict()
# create an instance of GetInvoiceResponse from a dict
get_invoice_response_from_dict = GetInvoiceResponse.from_dict(get_invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


