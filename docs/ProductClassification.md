# ProductClassification

Item classification identifier (BG-31).  Product classification according to a classification scheme.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_code** | **str** | Classification code (BT-158). | 
**list_id** | **str** |  | [optional] 
**list_version_id** | **str** |  | [optional] 

## Example

```python
from factpulse.models.product_classification import ProductClassification

# TODO update the JSON string below
json = "{}"
# create an instance of ProductClassification from a JSON string
product_classification_instance = ProductClassification.from_json(json)
# print the JSON string representation of the object
print(ProductClassification.to_json())

# convert the object into a dict
product_classification_dict = product_classification_instance.to_dict()
# create an instance of ProductClassification from a dict
product_classification_from_dict = ProductClassification.from_dict(product_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


