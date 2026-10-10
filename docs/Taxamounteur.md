# Taxamounteur

VAT amount in EUR for a non-EUR invoice. Computed automatically from the exchange rate when omitted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.taxamounteur import Taxamounteur

# TODO update the JSON string below
json = "{}"
# create an instance of Taxamounteur from a JSON string
taxamounteur_instance = Taxamounteur.from_json(json)
# print the JSON string representation of the object
print(Taxamounteur.to_json())

# convert the object into a dict
taxamounteur_dict = taxamounteur_instance.to_dict()
# create an instance of Taxamounteur from a dict
taxamounteur_from_dict = Taxamounteur.from_dict(taxamounteur_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


