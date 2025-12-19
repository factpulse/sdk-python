# TotalGrossAmount

Total gross amount (including tax). (Accepte number, string ou integer)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.total_gross_amount import TotalGrossAmount

# TODO update the JSON string below
json = "{}"
# create an instance of TotalGrossAmount from a JSON string
total_gross_amount_instance = TotalGrossAmount.from_json(json)
# print the JSON string representation of the object
print(TotalGrossAmount.to_json())

# convert the object into a dict
total_gross_amount_dict = total_gross_amount_instance.to_dict()
# create an instance of TotalGrossAmount from a dict
total_gross_amount_from_dict = TotalGrossAmount.from_dict(total_gross_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


