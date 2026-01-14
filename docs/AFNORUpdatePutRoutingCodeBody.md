# AFNORUpdatePutRoutingCodeBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routing_identifier_type** | **str** | Routing Identifier type. | 
**routing_code_name** | **str** | Name of the directory line routing code. This attribute is only returned if the directory line is defined at the SIREN / SIRET / Routing code mesh. | 
**administrative_status** | [**AFNORRoutingCodeAdministrativeStatus**](AFNORRoutingCodeAdministrativeStatus.md) |  | 
**address** | [**AFNORAddressPut**](AFNORAddressPut.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_update_put_routing_code_body import AFNORUpdatePutRoutingCodeBody

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORUpdatePutRoutingCodeBody from a JSON string
afnor_update_put_routing_code_body_instance = AFNORUpdatePutRoutingCodeBody.from_json(json)
# print the JSON string representation of the object
print(AFNORUpdatePutRoutingCodeBody.to_json())

# convert the object into a dict
afnor_update_put_routing_code_body_dict = afnor_update_put_routing_code_body_instance.to_dict()
# create an instance of AFNORUpdatePutRoutingCodeBody from a dict
afnor_update_put_routing_code_body_from_dict = AFNORUpdatePutRoutingCodeBody.from_dict(afnor_update_put_routing_code_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


