# PageDimensionsSchema

PDF page dimensions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **float** | Width in PDF points | 
**height** | **float** | Height in PDF points | 

## Example

```python
from factpulse.models.page_dimensions_schema import PageDimensionsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PageDimensionsSchema from a JSON string
page_dimensions_schema_instance = PageDimensionsSchema.from_json(json)
# print the JSON string representation of the object
print(PageDimensionsSchema.to_json())

# convert the object into a dict
page_dimensions_schema_dict = page_dimensions_schema_instance.to_dict()
# create an instance of PageDimensionsSchema from a dict
page_dimensions_schema_from_dict = PageDimensionsSchema.from_dict(page_dimensions_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


