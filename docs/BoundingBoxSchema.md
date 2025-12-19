# BoundingBoxSchema

Rectangular area coordinates in PDF.  Coordinates are in PDF points (1 point = 1/72 inch). Origin (0,0) is at the bottom-left of the page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x0** | **float** | Left X coordinate | 
**y0** | **float** | Bottom Y coordinate | 
**x1** | **float** | Right X coordinate | 
**y1** | **float** | Top Y coordinate | 
**page** | **int** | Page number (0-indexed) | [optional] [default to 0]
**width** | **float** | Area width | 
**height** | **float** | Area height | 

## Example

```python
from factpulse.models.bounding_box_schema import BoundingBoxSchema

# TODO update the JSON string below
json = "{}"
# create an instance of BoundingBoxSchema from a JSON string
bounding_box_schema_instance = BoundingBoxSchema.from_json(json)
# print the JSON string representation of the object
print(BoundingBoxSchema.to_json())

# convert the object into a dict
bounding_box_schema_dict = bounding_box_schema_instance.to_dict()
# create an instance of BoundingBoxSchema from a dict
bounding_box_schema_from_dict = BoundingBoxSchema.from_dict(bounding_box_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


