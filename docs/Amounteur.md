# Amounteur

Payment amount in EUR for a non-EUR payment (G6.27). Computed automatically from the exchange rate when omitted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.amounteur import Amounteur

# TODO update the JSON string below
json = "{}"
# create an instance of Amounteur from a JSON string
amounteur_instance = Amounteur.from_json(json)
# print the JSON string representation of the object
print(Amounteur.to_json())

# convert the object into a dict
amounteur_dict = amounteur_instance.to_dict()
# create an instance of Amounteur from a dict
amounteur_from_dict = Amounteur.from_dict(amounteur_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


