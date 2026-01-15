# StructureParameters

Mandatory structure parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_code_required** | **bool** | Service code is mandatory | [optional] [default to False]
**engagement_number_required** | **bool** | Engagement number is mandatory | [optional] [default to False]
**engagement_or_service_management** | **bool** | EJ or service code management enabled | [optional] [default to False]

## Example

```python
from factpulse.models.structure_parameters import StructureParameters

# TODO update the JSON string below
json = "{}"
# create an instance of StructureParameters from a JSON string
structure_parameters_instance = StructureParameters.from_json(json)
# print the JSON string representation of the object
print(StructureParameters.to_json())

# convert the object into a dict
structure_parameters_dict = structure_parameters_instance.to_dict()
# create an instance of StructureParameters from a dict
structure_parameters_from_dict = StructureParameters.from_dict(structure_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


