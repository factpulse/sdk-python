# Note

Note de facture (IncludedNote en Factur-X).  Les notes obligatoires pour BR-FR-05 sont : - PMT : Indemnité forfaitaire pour frais de recouvrement - PMD : Pénalités de retard - AAB : Escompte pour paiement anticipé

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject_code** | **str** |  | [optional] 
**content** | **str** |  | 

## Example

```python
from factpulse.models.note import Note

# TODO update the JSON string below
json = "{}"
# create an instance of Note from a JSON string
note_instance = Note.from_json(json)
# print the JSON string representation of the object
print(Note.to_json())

# convert the object into a dict
note_dict = note_instance.to_dict()
# create an instance of Note from a dict
note_from_dict = Note.from_dict(note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


