# ReponseHealthcheckAFNOR

Réponse du healthcheck des services AFNOR

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_service_ok** | **bool** | État du Flow Service API | 
**directory_service_ok** | **bool** | État du Directory Service API | 
**message** | **str** | Message descriptif de l&#39;état | 

## Example

```python
from factpulse.models.reponse_healthcheck_afnor import ReponseHealthcheckAFNOR

# TODO update the JSON string below
json = "{}"
# create an instance of ReponseHealthcheckAFNOR from a JSON string
reponse_healthcheck_afnor_instance = ReponseHealthcheckAFNOR.from_json(json)
# print the JSON string representation of the object
print(ReponseHealthcheckAFNOR.to_json())

# convert the object into a dict
reponse_healthcheck_afnor_dict = reponse_healthcheck_afnor_instance.to_dict()
# create an instance of ReponseHealthcheckAFNOR from a dict
reponse_healthcheck_afnor_from_dict = ReponseHealthcheckAFNOR.from_dict(reponse_healthcheck_afnor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


