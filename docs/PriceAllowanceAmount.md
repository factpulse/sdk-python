# PriceAllowanceAmount

Item price discount amount (BT-147).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.price_allowance_amount import PriceAllowanceAmount

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAllowanceAmount from a JSON string
price_allowance_amount_instance = PriceAllowanceAmount.from_json(json)
# print the JSON string representation of the object
print(PriceAllowanceAmount.to_json())

# convert the object into a dict
price_allowance_amount_dict = price_allowance_amount_instance.to_dict()
# create an instance of PriceAllowanceAmount from a dict
price_allowance_amount_from_dict = PriceAllowanceAmount.from_dict(price_allowance_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


