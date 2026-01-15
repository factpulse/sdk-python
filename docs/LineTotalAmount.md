# LineTotalAmount

Sum of all Invoice line net amounts (BT-106).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.line_total_amount import LineTotalAmount

# TODO update the JSON string below
json = "{}"
# create an instance of LineTotalAmount from a JSON string
line_total_amount_instance = LineTotalAmount.from_json(json)
# print the JSON string representation of the object
print(LineTotalAmount.to_json())

# convert the object into a dict
line_total_amount_dict = line_total_amount_instance.to_dict()
# create an instance of LineTotalAmount from a dict
line_total_amount_from_dict = LineTotalAmount.from_dict(line_total_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


