# ReponseValidationSucces


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message confirmant la conformité du XML. | 

## Example

```python
from factpulse.models.reponse_validation_succes import ReponseValidationSucces

# TODO update the JSON string below
json = "{}"
# create an instance of ReponseValidationSucces from a JSON string
reponse_validation_succes_instance = ReponseValidationSucces.from_json(json)
# print the JSON string representation of the object
print(ReponseValidationSucces.to_json())

# convert the object into a dict
reponse_validation_succes_dict = reponse_validation_succes_instance.to_dict()
# create an instance of ReponseValidationSucces from a dict
reponse_validation_succes_from_dict = ReponseValidationSucces.from_dict(reponse_validation_succes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


