# EnrichedInvoiceInfo

Information about the enriched invoice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_number** | **str** |  | 
**supplier_id** | **int** |  | [optional] 
**recipient_id** | **int** |  | [optional] 
**supplier_name** | **str** |  | 
**recipient_name** | **str** |  | 
**total_net_amount** | **str** |  | 
**vat_amount** | **str** |  | 
**total_gross_amount** | **str** |  | 

## Example

```python
from factpulse.models.enriched_invoice_info import EnrichedInvoiceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichedInvoiceInfo from a JSON string
enriched_invoice_info_instance = EnrichedInvoiceInfo.from_json(json)
# print the JSON string representation of the object
print(EnrichedInvoiceInfo.to_json())

# convert the object into a dict
enriched_invoice_info_dict = enriched_invoice_info_instance.to_dict()
# create an instance of EnrichedInvoiceInfo from a dict
enriched_invoice_info_from_dict = EnrichedInvoiceInfo.from_dict(enriched_invoice_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


