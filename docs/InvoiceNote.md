# InvoiceNote

Invoice note (IncludedNote in Factur-X).  Mandatory notes for BR-FR-05 are: - PMT: Fixed recovery fee - PMD: Late payment penalties - AAB: Early payment discount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject_code** | **str** |  | [optional] 
**content** | **str** | Note content | 

## Example

```python
from factpulse.models.invoice_note import InvoiceNote

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceNote from a JSON string
invoice_note_instance = InvoiceNote.from_json(json)
# print the JSON string representation of the object
print(InvoiceNote.to_json())

# convert the object into a dict
invoice_note_dict = invoice_note_instance.to_dict()
# create an instance of InvoiceNote from a dict
invoice_note_from_dict = InvoiceNote.from_dict(invoice_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


