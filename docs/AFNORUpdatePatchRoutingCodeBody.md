# AFNORUpdatePatchRoutingCodeBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routing_identifier_type** | **str** | Routing Identifier type. | [optional] 
**routing_code_name** | **str** | Name of the directory line routing code. This attribute is only returned if the directory line is defined at the SIREN / SIRET / Routing code mesh. | [optional] 
**administrative_status** | [**AFNORRoutingCodeAdministrativeStatus**](AFNORRoutingCodeAdministrativeStatus.md) |  | [optional] 
**address** | [**AFNORAddressPatch**](AFNORAddressPatch.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_update_patch_routing_code_body import AFNORUpdatePatchRoutingCodeBody

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORUpdatePatchRoutingCodeBody from a JSON string
afnor_update_patch_routing_code_body_instance = AFNORUpdatePatchRoutingCodeBody.from_json(json)
# print the JSON string representation of the object
print(AFNORUpdatePatchRoutingCodeBody.to_json())

# convert the object into a dict
afnor_update_patch_routing_code_body_dict = afnor_update_patch_routing_code_body_instance.to_dict()
# create an instance of AFNORUpdatePatchRoutingCodeBody from a dict
afnor_update_patch_routing_code_body_from_dict = AFNORUpdatePatchRoutingCodeBody.from_dict(afnor_update_patch_routing_code_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


