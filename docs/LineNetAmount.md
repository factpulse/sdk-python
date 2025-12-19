# LineNetAmount

Line net amount (quantity × unit price - allowance). (Accepte number, string ou integer)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.line_net_amount import LineNetAmount

# TODO update the JSON string below
json = "{}"
# create an instance of LineNetAmount from a JSON string
line_net_amount_instance = LineNetAmount.from_json(json)
# print the JSON string representation of the object
print(LineNetAmount.to_json())

# convert the object into a dict
line_net_amount_dict = line_net_amount_instance.to_dict()
# create an instance of LineNetAmount from a dict
line_net_amount_from_dict = LineNetAmount.from_dict(line_net_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


