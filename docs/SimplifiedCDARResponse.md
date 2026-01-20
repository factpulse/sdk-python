# SimplifiedCDARResponse

Réponse pour les endpoints CDAR simplifiés.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **str** | Identifiant du flux AFNOR | 
**document_id** | **str** | Identifiant du message CDAR généré | 
**status** | **str** | Code statut soumis (210 ou 212) | 
**invoice_id** | **str** | Identifiant de la facture | 
**message** | **str** | Message de confirmation | 

## Example

```python
from factpulse.models.simplified_cdar_response import SimplifiedCDARResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedCDARResponse from a JSON string
simplified_cdar_response_instance = SimplifiedCDARResponse.from_json(json)
# print the JSON string representation of the object
print(SimplifiedCDARResponse.to_json())

# convert the object into a dict
simplified_cdar_response_dict = simplified_cdar_response_instance.to_dict()
# create an instance of SimplifiedCDARResponse from a dict
simplified_cdar_response_from_dict = SimplifiedCDARResponse.from_dict(simplified_cdar_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


