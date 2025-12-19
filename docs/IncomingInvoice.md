# IncomingInvoice

Invoice received from a supplier via PDP/PA.  This model contains essential metadata extracted from incoming invoices, regardless of their source format (CII, UBL, Factur-X).  Amounts are Decimal in Python but will be serialized as strings in JSON to preserve monetary precision.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **str** |  | [optional] 
**source_format** | [**InvoiceFormat**](InvoiceFormat.md) | Invoice source format | 
**supplier_reference** | **str** | Invoice number issued by the supplier (BT-1) | 
**document_type** | [**DocumentType**](DocumentType.md) | Document type (BT-3) | [optional] 
**supplier** | [**IncomingSupplier**](IncomingSupplier.md) | Invoice issuer (SellerTradeParty) | 
**billing_site_name** | **str** | Recipient name / your company (BT-44) | 
**billing_site_siret** | **str** |  | [optional] 
**issue_date** | **str** | Invoice date (BT-2) - YYYY-MM-DD | 
**due_date** | **str** |  | [optional] 
**currency** | **str** | ISO currency code (BT-5) | [optional] [default to 'EUR']
**net_amount** | **str** | Total net amount (BT-109) | 
**vat_amount** | **str** | Total VAT amount (BT-110) | 
**gross_amount** | **str** | Total gross amount (BT-112) | 
**purchase_order_number** | **str** |  | [optional] 
**contract_reference** | **str** |  | [optional] 
**invoice_subject** | **str** |  | [optional] 
**document_base64** | **str** |  | [optional] 
**document_content_type** | **str** |  | [optional] 
**document_filename** | **str** |  | [optional] 

## Example

```python
from factpulse.models.incoming_invoice import IncomingInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingInvoice from a JSON string
incoming_invoice_instance = IncomingInvoice.from_json(json)
# print the JSON string representation of the object
print(IncomingInvoice.to_json())

# convert the object into a dict
incoming_invoice_dict = incoming_invoice_instance.to_dict()
# create an instance of IncomingInvoice from a dict
incoming_invoice_from_dict = IncomingInvoice.from_dict(incoming_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


