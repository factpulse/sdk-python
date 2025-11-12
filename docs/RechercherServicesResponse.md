# RechercherServicesResponse

Liste des services d'une structure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code_retour** | **int** |  | 
**libelle** | **str** |  | 
**liste_services** | [**List[ServiceStructure]**](ServiceStructure.md) |  | [optional] 
**total** | **int** | Nombre de services | [optional] [default to 0]

## Example

```python
from factpulse.models.rechercher_services_response import RechercherServicesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RechercherServicesResponse from a JSON string
rechercher_services_response_instance = RechercherServicesResponse.from_json(json)
# print the JSON string representation of the object
print(RechercherServicesResponse.to_json())

# convert the object into a dict
rechercher_services_response_dict = rechercher_services_response_instance.to_dict()
# create an instance of RechercherServicesResponse from a dict
rechercher_services_response_from_dict = RechercherServicesResponse.from_dict(rechercher_services_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


