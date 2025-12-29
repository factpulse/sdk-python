# RoundingAmount

Rounding amount added to total (BT-114).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.rounding_amount import RoundingAmount

# TODO update the JSON string below
json = "{}"
# create an instance of RoundingAmount from a JSON string
rounding_amount_instance = RoundingAmount.from_json(json)
# print the JSON string representation of the object
print(RoundingAmount.to_json())

# convert the object into a dict
rounding_amount_dict = rounding_amount_instance.to_dict()
# create an instance of RoundingAmount from a dict
rounding_amount_from_dict = RoundingAmount.from_dict(rounding_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


