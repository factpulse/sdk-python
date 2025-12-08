# BoundingBoxSchema

Coordonnées d'une zone rectangulaire dans le PDF.  Les coordonnées sont en points PDF (1 point = 1/72 pouce). L'origine (0,0) est en bas à gauche de la page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x0** | **float** | Coordonnée X gauche | 
**y0** | **float** | Coordonnée Y bas | 
**x1** | **float** | Coordonnée X droite | 
**y1** | **float** | Coordonnée Y haut | 
**page** | **int** | Numéro de page (0-indexed) | [optional] [default to 0]
**width** | **float** | Largeur de la zone | 
**height** | **float** | Hauteur de la zone | 

## Example

```python
from factpulse.models.bounding_box_schema import BoundingBoxSchema

# TODO update the JSON string below
json = "{}"
# create an instance of BoundingBoxSchema from a JSON string
bounding_box_schema_instance = BoundingBoxSchema.from_json(json)
# print the JSON string representation of the object
print(BoundingBoxSchema.to_json())

# convert the object into a dict
bounding_box_schema_dict = bounding_box_schema_instance.to_dict()
# create an instance of BoundingBoxSchema from a dict
bounding_box_schema_from_dict = BoundingBoxSchema.from_dict(bounding_box_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


