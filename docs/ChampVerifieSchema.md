# ChampVerifieSchema

Un champ vérifié avec toutes ses informations (extraction + conformité + localisation).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_term** | **str** | Business Term EN16931 (ex: BT-1) | 
**label** | **str** | Libellé du champ (ex: N° Facture) | 
**valeur_pdf** | **str** |  | [optional] 
**valeur_xml** | **str** |  | [optional] 
**statut** | [**StatutChampAPI**](StatutChampAPI.md) | Statut de conformité | 
**message** | **str** |  | [optional] 
**confiance** | **float** | Score de confiance (0-1) | [optional] [default to 1.0]
**source** | **str** | Source d&#39;extraction | [optional] [default to 'pdf_natif']
**bbox** | [**BoundingBoxSchema**](BoundingBoxSchema.md) |  | [optional] 

## Example

```python
from factpulse.models.champ_verifie_schema import ChampVerifieSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ChampVerifieSchema from a JSON string
champ_verifie_schema_instance = ChampVerifieSchema.from_json(json)
# print the JSON string representation of the object
print(ChampVerifieSchema.to_json())

# convert the object into a dict
champ_verifie_schema_dict = champ_verifie_schema_instance.to_dict()
# create an instance of ChampVerifieSchema from a dict
champ_verifie_schema_from_dict = ChampVerifieSchema.from_dict(champ_verifie_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


