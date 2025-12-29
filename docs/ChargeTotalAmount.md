# ChargeTotalAmount

Sum of all charges on document level (BT-108).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.charge_total_amount import ChargeTotalAmount

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeTotalAmount from a JSON string
charge_total_amount_instance = ChargeTotalAmount.from_json(json)
# print the JSON string representation of the object
print(ChargeTotalAmount.to_json())

# convert the object into a dict
charge_total_amount_dict = charge_total_amount_instance.to_dict()
# create an instance of ChargeTotalAmount from a dict
charge_total_amount_from_dict = ChargeTotalAmount.from_dict(charge_total_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


