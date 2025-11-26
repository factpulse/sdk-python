# ValidationErrorDetail

Détail d'une erreur de validation (aligné sur AFNOR AcknowledgementDetail).  Format unifié pour toutes les erreurs de validation Factur-X, compatible avec la norme AFNOR XP Z12-013.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | [**ErrorLevel**](ErrorLevel.md) | Niveau de gravité : &#39;Error&#39; ou &#39;Warning&#39; | [optional] 
**item** | **str** | Identifiant de l&#39;élément concerné (XPath, champ, règle BR-FR, etc.) | 
**reason** | **str** | Description de l&#39;erreur | 
**source** | [**ErrorSource**](ErrorSource.md) |  | [optional] 
**code** | **str** |  | [optional] 

## Example

```python
from factpulse.models.validation_error_detail import ValidationErrorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationErrorDetail from a JSON string
validation_error_detail_instance = ValidationErrorDetail.from_json(json)
# print the JSON string representation of the object
print(ValidationErrorDetail.to_json())

# convert the object into a dict
validation_error_detail_dict = validation_error_detail_instance.to_dict()
# create an instance of ValidationErrorDetail from a dict
validation_error_detail_from_dict = ValidationErrorDetail.from_dict(validation_error_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


