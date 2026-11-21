# Amount2

Montant TTC encaissé en EUR, à un seul taux (vatRate). Négatif pour un décaissement (remboursement). Pour plusieurs taux, utiliser amountsByRate. Requis si amountsByRate est absent (BR-FR-CDV-14)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.amount2 import Amount2

# TODO update the JSON string below
json = "{}"
# create an instance of Amount2 from a JSON string
amount2_instance = Amount2.from_json(json)
# print the JSON string representation of the object
print(Amount2.to_json())

# convert the object into a dict
amount2_dict = amount2_instance.to_dict()
# create an instance of Amount2 from a dict
amount2_from_dict = Amount2.from_dict(amount2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


