# MontantTvaTotal

Montant total de la TVA. (Accepte number, string ou integer)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.montant_tva_total import MontantTvaTotal

# TODO update the JSON string below
json = "{}"
# create an instance of MontantTvaTotal from a JSON string
montant_tva_total_instance = MontantTvaTotal.from_json(json)
# print the JSON string representation of the object
print(MontantTvaTotal.to_json())

# convert the object into a dict
montant_tva_total_dict = montant_tva_total_instance.to_dict()
# create an instance of MontantTvaTotal from a dict
montant_tva_total_from_dict = MontantTvaTotal.from_dict(montant_tva_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


