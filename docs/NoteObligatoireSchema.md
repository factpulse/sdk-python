# NoteObligatoireSchema

Note obligatoire détectée avec localisation et comparaison XML/PDF.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code_sujet** | **str** | Code sujet (PMT, PMD, AAB) | 
**label** | **str** | Libellé (ex: Indemnité recouvrement) | 
**valeur_pdf** | **str** |  | [optional] 
**valeur_xml** | **str** |  | [optional] 
**statut** | [**StatutChampAPI**](StatutChampAPI.md) | Statut de conformité (CONFORME si XML trouvé dans PDF) | [optional] 
**message** | **str** |  | [optional] 
**bbox** | [**BoundingBoxSchema**](BoundingBoxSchema.md) |  | [optional] 

## Example

```python
from factpulse.models.note_obligatoire_schema import NoteObligatoireSchema

# TODO update the JSON string below
json = "{}"
# create an instance of NoteObligatoireSchema from a JSON string
note_obligatoire_schema_instance = NoteObligatoireSchema.from_json(json)
# print the JSON string representation of the object
print(NoteObligatoireSchema.to_json())

# convert the object into a dict
note_obligatoire_schema_dict = note_obligatoire_schema_instance.to_dict()
# create an instance of NoteObligatoireSchema from a dict
note_obligatoire_schema_from_dict = NoteObligatoireSchema.from_dict(note_obligatoire_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


