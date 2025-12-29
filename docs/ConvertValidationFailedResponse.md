# ConvertValidationFailedResponse

Reponse echec de validation - inclut les donnees extraites pour correction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] [default to 'validation_failed']
**conversion_id** | **str** |  | 
**message** | **str** |  | [optional] [default to 'Donnees extraites avec erreurs de validation. Completez le formulaire et appelez /resume.']
**extraction** | [**ExtractionInfo**](ExtractionInfo.md) |  | 
**extracted_data** | **Dict[str, object]** | Donnees extraites par OCR au format FacturXInvoice (a completer/corriger) | 
**missing_fields** | [**List[MissingField]**](MissingField.md) | Champs manquants pour conformite Factur-X | [optional] 
**validation** | [**ValidationInfo**](ValidationInfo.md) |  | 
**resume_url** | **str** | URL pour reprendre la conversion avec corrections | 
**expires_at** | **datetime** | Expiration de la conversion (1h) | 

## Example

```python
from factpulse.models.convert_validation_failed_response import ConvertValidationFailedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertValidationFailedResponse from a JSON string
convert_validation_failed_response_instance = ConvertValidationFailedResponse.from_json(json)
# print the JSON string representation of the object
print(ConvertValidationFailedResponse.to_json())

# convert the object into a dict
convert_validation_failed_response_dict = convert_validation_failed_response_instance.to_dict()
# create an instance of ConvertValidationFailedResponse from a dict
convert_validation_failed_response_from_dict = ConvertValidationFailedResponse.from_dict(convert_validation_failed_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


