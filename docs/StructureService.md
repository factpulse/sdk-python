# StructureService

Structure service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **int** | Service ID | 
**service_code** | **str** | Service code | 
**service_label** | **str** | Service label | 
**is_active** | **bool** | Service active | 

## Example

```python
from factpulse.models.structure_service import StructureService

# TODO update the JSON string below
json = "{}"
# create an instance of StructureService from a JSON string
structure_service_instance = StructureService.from_json(json)
# print the JSON string representation of the object
print(StructureService.to_json())

# convert the object into a dict
structure_service_dict = structure_service_instance.to_dict()
# create an instance of StructureService from a dict
structure_service_from_dict = StructureService.from_dict(structure_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


