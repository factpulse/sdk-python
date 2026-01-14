# PriceBasisQuantity

Item price base quantity (BT-149). Default is 1.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.price_basis_quantity import PriceBasisQuantity

# TODO update the JSON string below
json = "{}"
# create an instance of PriceBasisQuantity from a JSON string
price_basis_quantity_instance = PriceBasisQuantity.from_json(json)
# print the JSON string representation of the object
print(PriceBasisQuantity.to_json())

# convert the object into a dict
price_basis_quantity_dict = price_basis_quantity_instance.to_dict()
# create an instance of PriceBasisQuantity from a dict
price_basis_quantity_from_dict = PriceBasisQuantity.from_dict(price_basis_quantity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


