# SubmitCompleteInvoiceRequest

Request to submit a complete invoice (generation + submission).  Workflow: 1. Auto-enrichment (optional) 2. Factur-X PDF generation 3. Signature (optional) 4. Submission to destination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_data** | [**SimplifiedInvoiceData**](SimplifiedInvoiceData.md) | Invoice data in simplified format (see examples) | 
**source_pdf** | **str** | Base64-encoded source PDF (will be transformed to Factur-X) | 
**destination** | [**Destination**](Destination.md) |  | 
**signature** | [**SignatureParameters**](SignatureParameters.md) |  | [optional] 
**options** | [**ProcessingOptions**](ProcessingOptions.md) | Processing options | [optional] 

## Example

```python
from factpulse.models.submit_complete_invoice_request import SubmitCompleteInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitCompleteInvoiceRequest from a JSON string
submit_complete_invoice_request_instance = SubmitCompleteInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(SubmitCompleteInvoiceRequest.to_json())

# convert the object into a dict
submit_complete_invoice_request_dict = submit_complete_invoice_request_instance.to_dict()
# create an instance of SubmitCompleteInvoiceRequest from a dict
submit_complete_invoice_request_from_dict = SubmitCompleteInvoiceRequest.from_dict(submit_complete_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


