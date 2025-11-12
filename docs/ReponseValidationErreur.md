# ReponseValidationErreur


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **List[str]** | Liste des erreurs de validation détectées. | 

## Example

```python
from factpulse.models.reponse_validation_erreur import ReponseValidationErreur

# TODO update the JSON string below
json = "{}"
# create an instance of ReponseValidationErreur from a JSON string
reponse_validation_erreur_instance = ReponseValidationErreur.from_json(json)
# print the JSON string representation of the object
print(ReponseValidationErreur.to_json())

# convert the object into a dict
reponse_validation_erreur_dict = reponse_validation_erreur_instance.to_dict()
# create an instance of ReponseValidationErreur from a dict
reponse_validation_erreur_from_dict = ReponseValidationErreur.from_dict(reponse_validation_erreur_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


