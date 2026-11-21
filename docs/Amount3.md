# Amount3

Collected amount for this VAT rate (TT-95 / TT-99). Negative for a refund, on the refund date (G7.07)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.amount3 import Amount3

# TODO update the JSON string below
json = "{}"
# create an instance of Amount3 from a JSON string
amount3_instance = Amount3.from_json(json)
# print the JSON string representation of the object
print(Amount3.to_json())

# convert the object into a dict
amount3_dict = amount3_instance.to_dict()
# create an instance of Amount3 from a dict
amount3_from_dict = Amount3.from_dict(amount3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


