# BaseAmount

Base amount for percentage calculation (BT-93/100/137/142).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.base_amount import BaseAmount

# TODO update the JSON string below
json = "{}"
# create an instance of BaseAmount from a JSON string
base_amount_instance = BaseAmount.from_json(json)
# print the JSON string representation of the object
print(BaseAmount.to_json())

# convert the object into a dict
base_amount_dict = base_amount_instance.to_dict()
# create an instance of BaseAmount from a dict
base_amount_from_dict = BaseAmount.from_dict(base_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


