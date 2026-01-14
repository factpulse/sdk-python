# AFNORRoutingCodePost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_instance** | **int** | Platform instance identifier in the directory | [optional] 
**siret** | **str** | SIRET Number | [optional] 
**routing_identifier** | **str** | Routing identifier od a routing code. | [optional] 

## Example

```python
from factpulse.models.afnor_routing_code_post201_response import AFNORRoutingCodePost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORRoutingCodePost201Response from a JSON string
afnor_routing_code_post201_response_instance = AFNORRoutingCodePost201Response.from_json(json)
# print the JSON string representation of the object
print(AFNORRoutingCodePost201Response.to_json())

# convert the object into a dict
afnor_routing_code_post201_response_dict = afnor_routing_code_post201_response_instance.to_dict()
# create an instance of AFNORRoutingCodePost201Response from a dict
afnor_routing_code_post201_response_from_dict = AFNORRoutingCodePost201Response.from_dict(afnor_routing_code_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


