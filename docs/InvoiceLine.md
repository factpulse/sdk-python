# InvoiceLine

Represents an invoice line item (BG-25).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_number** | **int** | Invoice line identifier (BT-126). | 
**line_note** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**buyer_assigned_id** | **str** |  | [optional] 
**product_global_id** | **str** |  | [optional] 
**product_global_id_scheme** | **str** |  | [optional] 
**item_name** | **str** | Item name (BT-153). | 
**item_description** | **str** |  | [optional] 
**origin_country** | **str** |  | [optional] 
**characteristics** | [**List[ProductCharacteristic]**](ProductCharacteristic.md) |  | [optional] 
**classifications** | [**List[ProductClassification]**](ProductClassification.md) |  | [optional] 
**quantity** | [**Quantity**](Quantity.md) |  | 
**unit** | [**UnitOfMeasure**](UnitOfMeasure.md) | Invoiced quantity unit of measure code (BT-130). | 
**gross_unit_price** | [**GrossUnitPrice**](GrossUnitPrice.md) |  | [optional] 
**unit_net_price** | [**UnitNetPrice**](UnitNetPrice.md) |  | 
**price_basis_quantity** | [**PriceBasisQuantity**](PriceBasisQuantity.md) |  | [optional] 
**price_basis_unit** | **str** |  | [optional] 
**price_allowance_amount** | [**PriceAllowanceAmount**](PriceAllowanceAmount.md) |  | [optional] 
**line_net_amount** | [**LineNetAmount**](LineNetAmount.md) |  | [optional] 
**allowance_amount** | [**InvoiceLineAllowanceAmount**](InvoiceLineAllowanceAmount.md) |  | [optional] 
**allowance_reason_code** | [**AllowanceReasonCode**](AllowanceReasonCode.md) |  | [optional] 
**allowance_reason** | **str** |  | [optional] 
**allowances_charges** | [**List[AllowanceCharge]**](AllowanceCharge.md) |  | [optional] 
**vat_rate** | **str** |  | [optional] 
**manual_vat_rate** | [**ManualVatRate**](ManualVatRate.md) |  | [optional] 
**vat_category** | [**VATCategory**](VATCategory.md) |  | [optional] 
**period_start_date** | **str** |  | [optional] 
**period_end_date** | **str** |  | [optional] 
**purchase_order_line_ref** | **str** |  | [optional] 
**accounting_account** | **str** |  | [optional] 
**additional_documents** | [**List[AdditionalDocument]**](AdditionalDocument.md) |  | [optional] 
**line_notes** | [**List[InvoiceNote]**](InvoiceNote.md) |  | [optional] 

## Example

```python
from factpulse.models.invoice_line import InvoiceLine

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceLine from a JSON string
invoice_line_instance = InvoiceLine.from_json(json)
# print the JSON string representation of the object
print(InvoiceLine.to_json())

# convert the object into a dict
invoice_line_dict = invoice_line_instance.to_dict()
# create an instance of InvoiceLine from a dict
invoice_line_from_dict = InvoiceLine.from_dict(invoice_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


