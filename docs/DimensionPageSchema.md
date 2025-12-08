# DimensionPageSchema

Dimensions d'une page PDF.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **float** | Largeur en points PDF | 
**height** | **float** | Hauteur en points PDF | 

## Example

```python
from factpulse.models.dimension_page_schema import DimensionPageSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DimensionPageSchema from a JSON string
dimension_page_schema_instance = DimensionPageSchema.from_json(json)
# print the JSON string representation of the object
print(DimensionPageSchema.to_json())

# convert the object into a dict
dimension_page_schema_dict = dimension_page_schema_instance.to_dict()
# create an instance of DimensionPageSchema from a dict
dimension_page_schema_from_dict = DimensionPageSchema.from_dict(dimension_page_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


