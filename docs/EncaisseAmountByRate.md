# EncaisseAmountByRate

Montant encaissé TTC pour un taux de TVA (un bloc MEN, MDG-43).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate** | **float** | Taux de TVA applicable au montant encaissé, en % (MDT-224) | 
**amount** | [**Amount1**](Amount1.md) |  | 

## Example

```python
from factpulse.models.encaisse_amount_by_rate import EncaisseAmountByRate

# TODO update the JSON string below
json = "{}"
# create an instance of EncaisseAmountByRate from a JSON string
encaisse_amount_by_rate_instance = EncaisseAmountByRate.from_json(json)
# print the JSON string representation of the object
print(EncaisseAmountByRate.to_json())

# convert the object into a dict
encaisse_amount_by_rate_dict = encaisse_amount_by_rate_instance.to_dict()
# create an instance of EncaisseAmountByRate from a dict
encaisse_amount_by_rate_from_dict = EncaisseAmountByRate.from_dict(encaisse_amount_by_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


