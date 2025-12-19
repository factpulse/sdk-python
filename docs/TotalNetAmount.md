# TotalNetAmount

Total net amount (before tax). (Accepte number, string ou integer)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.total_net_amount import TotalNetAmount

# TODO update the JSON string below
json = "{}"
# create an instance of TotalNetAmount from a JSON string
total_net_amount_instance = TotalNetAmount.from_json(json)
# print the JSON string representation of the object
print(TotalNetAmount.to_json())

# convert the object into a dict
total_net_amount_dict = total_net_amount_instance.to_dict()
# create an instance of TotalNetAmount from a dict
total_net_amount_from_dict = TotalNetAmount.from_dict(total_net_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


