# SimplifiedInvoiceData

Simplified invoice data (minimal format for auto-enrichment).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Unique invoice number | 
**supplier** | **Dict[str, object]** | Supplier information (siret, iban, ...) | 
**recipient** | **Dict[str, object]** | Recipient information (siret, ...) | 
**lines** | **List[Dict[str, object]]** | Invoice lines | 
**var_date** | **str** |  | [optional] 
**due_days** | **int** | Due date in days (default: 30) | [optional] [default to 30]
**comment** | **str** |  | [optional] 
**purchase_order_reference** | **str** |  | [optional] 
**contract_reference** | **str** |  | [optional] 
**invoice_type** | [**FactureElectroniqueModelsInvoiceTypeCode**](FactureElectroniqueModelsInvoiceTypeCode.md) | Document type (UNTDID 1001). Default: 380 (Invoice). | [optional] 
**preceding_invoice_reference** | **str** |  | [optional] 
**operation_nature** | [**OperationNature**](OperationNature.md) |  | [optional] 
**invoicing_framework** | [**InvoicingFrameworkCode**](InvoicingFrameworkCode.md) |  | [optional] 

## Example

```python
from factpulse.models.simplified_invoice_data import SimplifiedInvoiceData

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedInvoiceData from a JSON string
simplified_invoice_data_instance = SimplifiedInvoiceData.from_json(json)
# print the JSON string representation of the object
print(SimplifiedInvoiceData.to_json())

# convert the object into a dict
simplified_invoice_data_dict = simplified_invoice_data_instance.to_dict()
# create an instance of SimplifiedInvoiceData from a dict
simplified_invoice_data_from_dict = SimplifiedInvoiceData.from_dict(simplified_invoice_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


