# APIError

Erreur API standardisée (alignée sur AFNOR Error schema).  Format unifié pour toutes les réponses d'erreur HTTP.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** | Code alphanumérique identifiant précisément l&#39;erreur | 
**error_message** | **str** | Message décrivant l&#39;erreur (non destiné à l&#39;utilisateur final) | 
**details** | [**List[ValidationErrorDetail]**](ValidationErrorDetail.md) |  | [optional] 

## Example

```python
from factpulse.models.api_error import APIError

# TODO update the JSON string below
json = "{}"
# create an instance of APIError from a JSON string
api_error_instance = APIError.from_json(json)
# print the JSON string representation of the object
print(APIError.to_json())

# convert the object into a dict
api_error_dict = api_error_instance.to_dict()
# create an instance of APIError from a dict
api_error_from_dict = APIError.from_dict(api_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


