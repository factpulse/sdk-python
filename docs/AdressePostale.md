# AdressePostale

Représente une adresse postale.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code_postal** | **str** |  | [optional] 
**ligne_un** | **str** |  | [optional] 
**ligne_deux** | **str** |  | [optional] 
**nom_ville** | **str** |  | [optional] 
**pays_code_iso** | **str** |  | [optional] 

## Example

```python
from factpulse.models.adresse_postale import AdressePostale

# TODO update the JSON string below
json = "{}"
# create an instance of AdressePostale from a JSON string
adresse_postale_instance = AdressePostale.from_json(json)
# print the JSON string representation of the object
print(AdressePostale.to_json())

# convert the object into a dict
adresse_postale_dict = adresse_postale_instance.to_dict()
# create an instance of AdressePostale from a dict
adresse_postale_from_dict = AdressePostale.from_dict(adresse_postale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


