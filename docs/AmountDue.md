# AmountDue

Amount due for payment (BT-115). Can be negative for correction invoices.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.amount_due import AmountDue

# TODO update the JSON string below
json = "{}"
# create an instance of AmountDue from a JSON string
amount_due_instance = AmountDue.from_json(json)
# print the JSON string representation of the object
print(AmountDue.to_json())

# convert the object into a dict
amount_due_dict = amount_due_instance.to_dict()
# create an instance of AmountDue from a dict
amount_due_from_dict = AmountDue.from_dict(amount_due_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


