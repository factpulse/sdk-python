# ConsulterFactureRequest

Consulter une facture.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**ChorusProCredentials**](ChorusProCredentials.md) |  | [optional] 
**identifiant_facture_cpp** | **int** | ID Chorus Pro de la facture | 

## Example

```python
from factpulse.models.consulter_facture_request import ConsulterFactureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConsulterFactureRequest from a JSON string
consulter_facture_request_instance = ConsulterFactureRequest.from_json(json)
# print the JSON string representation of the object
print(ConsulterFactureRequest.to_json())

# convert the object into a dict
consulter_facture_request_dict = consulter_facture_request_instance.to_dict()
# create an instance of ConsulterFactureRequest from a dict
consulter_facture_request_from_dict = ConsulterFactureRequest.from_dict(consulter_facture_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


