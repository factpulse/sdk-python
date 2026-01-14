# MandatoryNoteSchema

Mandatory note detected with location and XML/PDF comparison.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject_code** | **str** | Subject code (PMT, PMD, AAB) | 
**label** | **str** | Label (e.g., Recovery indemnity) | 
**pdf_value** | **str** |  | [optional] 
**xml_value** | **str** |  | [optional] 
**status** | [**FieldStatus**](FieldStatus.md) | Compliance status (COMPLIANT if XML found in PDF) | [optional] 
**message** | **str** |  | [optional] 
**bbox** | [**BoundingBoxSchema**](BoundingBoxSchema.md) |  | [optional] 

## Example

```python
from factpulse.models.mandatory_note_schema import MandatoryNoteSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MandatoryNoteSchema from a JSON string
mandatory_note_schema_instance = MandatoryNoteSchema.from_json(json)
# print the JSON string representation of the object
print(MandatoryNoteSchema.to_json())

# convert the object into a dict
mandatory_note_schema_dict = mandatory_note_schema_instance.to_dict()
# create an instance of MandatoryNoteSchema from a dict
mandatory_note_schema_from_dict = MandatoryNoteSchema.from_dict(mandatory_note_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


