# GlobalAllowanceAmount

Global allowance amount (legacy - use allowance_total_amount). (Accepte number, string ou integer)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.global_allowance_amount import GlobalAllowanceAmount

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalAllowanceAmount from a JSON string
global_allowance_amount_instance = GlobalAllowanceAmount.from_json(json)
# print the JSON string representation of the object
print(GlobalAllowanceAmount.to_json())

# convert the object into a dict
global_allowance_amount_dict = global_allowance_amount_instance.to_dict()
# create an instance of GlobalAllowanceAmount from a dict
global_allowance_amount_from_dict = GlobalAllowanceAmount.from_dict(global_allowance_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


