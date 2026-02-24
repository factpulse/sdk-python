# ValidateCDARResponse

Réponse de validation CDAR.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** | Résultat de validation | 
**errors** | [**List[ValidationErrorResponse]**](ValidationErrorResponse.md) | Liste des erreurs | [optional] 
**warnings** | [**List[ValidationErrorResponse]**](ValidationErrorResponse.md) | Liste des avertissements | [optional] 

## Example

```python
from factpulse.models.validate_cdar_response import ValidateCDARResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateCDARResponse from a JSON string
validate_cdar_response_instance = ValidateCDARResponse.from_json(json)
# print the JSON string representation of the object
print(ValidateCDARResponse.to_json())

# convert the object into a dict
validate_cdar_response_dict = validate_cdar_response_instance.to_dict()
# create an instance of ValidateCDARResponse from a dict
validate_cdar_response_from_dict = ValidateCDARResponse.from_dict(validate_cdar_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


