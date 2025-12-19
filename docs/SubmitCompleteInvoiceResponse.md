# SubmitCompleteInvoiceResponse

Complete response after automated submission.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Invoice was successfully submitted | 
**destination_type** | **str** | Destination type | 
**chorus_result** | [**ChorusProResult**](ChorusProResult.md) |  | [optional] 
**afnor_result** | [**AFNORResult**](AFNORResult.md) |  | [optional] 
**enriched_invoice** | [**EnrichedInvoiceInfo**](EnrichedInvoiceInfo.md) | Enriched invoice data | 
**facturx_pdf** | [**FacturXPDFInfo**](FacturXPDFInfo.md) | Generated PDF information | 
**signature** | [**SignatureInfo**](SignatureInfo.md) |  | [optional] 
**pdf_base64** | **str** | Generated Factur-X PDF (and signed if requested) base64-encoded | 
**message** | **str** | Return message | 

## Example

```python
from factpulse.models.submit_complete_invoice_response import SubmitCompleteInvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitCompleteInvoiceResponse from a JSON string
submit_complete_invoice_response_instance = SubmitCompleteInvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(SubmitCompleteInvoiceResponse.to_json())

# convert the object into a dict
submit_complete_invoice_response_dict = submit_complete_invoice_response_instance.to_dict()
# create an instance of SubmitCompleteInvoiceResponse from a dict
submit_complete_invoice_response_from_dict = SubmitCompleteInvoiceResponse.from_dict(submit_complete_invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


