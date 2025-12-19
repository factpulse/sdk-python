# VerifiedFieldSchema

A verified field with all its information (extraction + compliance + location).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_term** | **str** | EN16931 Business Term (e.g., BT-1) | 
**label** | **str** | Field label (e.g., Invoice Number) | 
**pdf_value** | **str** |  | [optional] 
**xml_value** | **str** |  | [optional] 
**status** | [**FieldStatus**](FieldStatus.md) | Compliance status | 
**message** | **str** |  | [optional] 
**confidence** | **float** | Confidence score (0-1) | [optional] [default to 1.0]
**source** | **str** | Extraction source | [optional] [default to 'native_pdf']
**bbox** | [**BoundingBoxSchema**](BoundingBoxSchema.md) |  | [optional] 

## Example

```python
from factpulse.models.verified_field_schema import VerifiedFieldSchema

# TODO update the JSON string below
json = "{}"
# create an instance of VerifiedFieldSchema from a JSON string
verified_field_schema_instance = VerifiedFieldSchema.from_json(json)
# print the JSON string representation of the object
print(VerifiedFieldSchema.to_json())

# convert the object into a dict
verified_field_schema_dict = verified_field_schema_instance.to_dict()
# create an instance of VerifiedFieldSchema from a dict
verified_field_schema_from_dict = VerifiedFieldSchema.from_dict(verified_field_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


