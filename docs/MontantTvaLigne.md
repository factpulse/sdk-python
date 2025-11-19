# MontantTvaLigne

Montant de la TVA pour cette ligne.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.montant_tva_ligne import MontantTvaLigne

# TODO update the JSON string below
json = "{}"
# create an instance of MontantTvaLigne from a JSON string
montant_tva_ligne_instance = MontantTvaLigne.from_json(json)
# print the JSON string representation of the object
print(MontantTvaLigne.to_json())

# convert the object into a dict
montant_tva_ligne_dict = montant_tva_ligne_instance.to_dict()
# create an instance of MontantTvaLigne from a dict
montant_tva_ligne_from_dict = MontantTvaLigne.from_dict(montant_tva_ligne_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


