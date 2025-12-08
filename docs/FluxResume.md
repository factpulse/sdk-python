# FluxResume

Résumé d'un flux dans les résultats de recherche

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **str** |  | 
**tracking_id** | **str** |  | [optional] 
**nom** | **str** |  | 
**type_flux** | **str** |  | [optional] 
**direction_flux** | **str** |  | [optional] 
**statut_acquittement** | **str** |  | [optional] 
**date_creation** | **str** |  | [optional] 
**date_maj** | **str** |  | [optional] 

## Example

```python
from factpulse.models.flux_resume import FluxResume

# TODO update the JSON string below
json = "{}"
# create an instance of FluxResume from a JSON string
flux_resume_instance = FluxResume.from_json(json)
# print the JSON string representation of the object
print(FluxResume.to_json())

# convert the object into a dict
flux_resume_dict = flux_resume_instance.to_dict()
# create an instance of FluxResume from a dict
flux_resume_from_dict = FluxResume.from_dict(flux_resume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


