# Tauxmanuel

Taux de TVA avec valeur manuelle. (Accepte number, string ou integer)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from factpulse.models.tauxmanuel import Tauxmanuel

# TODO update the JSON string below
json = "{}"
# create an instance of Tauxmanuel from a JSON string
tauxmanuel_instance = Tauxmanuel.from_json(json)
# print the JSON string representation of the object
print(Tauxmanuel.to_json())

# convert the object into a dict
tauxmanuel_dict = tauxmanuel_instance.to_dict()
# create an instance of Tauxmanuel from a dict
tauxmanuel_from_dict = Tauxmanuel.from_dict(tauxmanuel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


