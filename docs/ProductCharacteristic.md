# ProductCharacteristic

Item attribute (BG-32).  Additional product characteristics as key-value pairs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Attribute name (BT-160). | 
**value** | **str** | Attribute value (BT-161). | 

## Example

```python
from factpulse.models.product_characteristic import ProductCharacteristic

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCharacteristic from a JSON string
product_characteristic_instance = ProductCharacteristic.from_json(json)
# print the JSON string representation of the object
print(ProductCharacteristic.to_json())

# convert the object into a dict
product_characteristic_dict = product_characteristic_instance.to_dict()
# create an instance of ProductCharacteristic from a dict
product_characteristic_from_dict = ProductCharacteristic.from_dict(product_characteristic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


