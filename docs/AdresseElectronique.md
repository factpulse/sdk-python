# AdresseElectronique

Représente une adresse de facturation électronique, composée d'un identifiant et de son schéma (SchemeID) conformément à la norme EN16931. Exemple: { \"identifiant\": \"123456789\", \"scheme_id\": \"0225\" }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiant** | **str** |  | 
**scheme_id** | [**SchemeID**](SchemeID.md) |  | [optional] 

## Example

```python
from factpulse.models.adresse_electronique import AdresseElectronique

# TODO update the JSON string below
json = "{}"
# create an instance of AdresseElectronique from a JSON string
adresse_electronique_instance = AdresseElectronique.from_json(json)
# print the JSON string representation of the object
print(AdresseElectronique.to_json())

# convert the object into a dict
adresse_electronique_dict = adresse_electronique_instance.to_dict()
# create an instance of AdresseElectronique from a dict
adresse_electronique_from_dict = AdresseElectronique.from_dict(adresse_electronique_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


