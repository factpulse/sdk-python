# ExtractionInfo

Informations sur l'extraction des donnees.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence_score** | **float** | Score de confiance global (0-1) | 
**fields_extracted** | **int** | Nombre de champs extraits | 
**fields_enriched** | **int** | Nombre de champs enrichis automatiquement | [optional] [default to 0]
**fields_missing** | **int** | Nombre de champs manquants | [optional] [default to 0]

## Example

```python
from factpulse.models.extraction_info import ExtractionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractionInfo from a JSON string
extraction_info_instance = ExtractionInfo.from_json(json)
# print the JSON string representation of the object
print(ExtractionInfo.to_json())

# convert the object into a dict
extraction_info_dict = extraction_info_instance.to_dict()
# create an instance of ExtractionInfo from a dict
extraction_info_from_dict = ExtractionInfo.from_dict(extraction_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


