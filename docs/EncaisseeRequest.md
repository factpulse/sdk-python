# EncaisseeRequest

Requête simplifiée pour soumettre un statut ENCAISSÉE (212).  **Usage** : Pour une facture ÉMISE (vous êtes vendeur). Le vendeur confirme l'encaissement et envoie le statut à l'acheteur.  Statut obligatoire PPF - Le montant encaissé est OBLIGATOIRE (BR-FR-CDV-14).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Identifiant de la facture (BT-1) | 
**invoice_issue_date** | **date** | Date d&#39;émission de la facture (YYYY-MM-DD) | 
**invoice_buyer_siren** | **str** | SIREN de l&#39;acheteur (destinataire du statut) | 
**invoice_buyer_electronic_address** | **str** | Adresse électronique de l&#39;acheteur (MDT-73) | 
**amount** | [**Amount**](Amount.md) |  | 
**currency** | **str** | Code devise ISO 4217 | [optional] [default to 'EUR']
**sender_siren** | **str** |  | [optional] 
**flow_type** | **str** | Type de flux (CustomerInvoiceLC pour facture émise) | [optional] [default to 'CustomerInvoiceLC']
**pdp_flow_service_url** | **str** |  | [optional] 
**pdp_token_url** | **str** |  | [optional] 
**pdp_client_id** | **str** |  | [optional] 
**pdp_client_secret** | **str** |  | [optional] 

## Example

```python
from factpulse.models.encaissee_request import EncaisseeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EncaisseeRequest from a JSON string
encaissee_request_instance = EncaisseeRequest.from_json(json)
# print the JSON string representation of the object
print(EncaisseeRequest.to_json())

# convert the object into a dict
encaissee_request_dict = encaissee_request_instance.to_dict()
# create an instance of EncaisseeRequest from a dict
encaissee_request_from_dict = EncaisseeRequest.from_dict(encaissee_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


