# SubmitCDARRequest

Requête de soumission CDAR (génération + envoi).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Identifiant unique du message CDAR | 
**business_process** | **str** | Code processus métier (REGULATED, B2C, B2BINT, etc.) | [optional] [default to 'REGULATED']
**type_code** | **str** | Type de message (23&#x3D;Traitement, 305&#x3D;Transmission) | [optional] [default to '23']
**sender_siren** | **str** | SIREN de l&#39;émetteur (9 chiffres) | 
**sender_role** | **str** | Rôle de l&#39;émetteur (WK, SE, BY, etc.) | [optional] [default to 'WK']
**sender_name** | **str** |  | [optional] 
**sender_email** | **str** |  | [optional] 
**recipients** | [**List[RecipientInput]**](RecipientInput.md) | Liste des destinataires | [optional] 
**invoice_id** | **str** | Identifiant de la facture (BT-1) | 
**invoice_issue_date** | **date** | Date d&#39;émission de la facture (YYYY-MM-DD) | 
**invoice_type_code** | **str** | Type de document (380&#x3D;Facture, 381&#x3D;Avoir) | [optional] [default to '380']
**invoice_seller_siren** | **str** |  | [optional] 
**invoice_buyer_siren** | **str** |  | [optional] 
**status** | **str** | Code statut de la facture (200-601) | 
**reason_code** | **str** |  | [optional] 
**reason_text** | **str** |  | [optional] 
**action_code** | **str** |  | [optional] 
**encaisse_amount** | [**Encaisseamount**](Encaisseamount.md) |  | [optional] 
**flow_type** | **str** | Type de flux AFNOR (CustomerInvoiceLC, SupplierInvoiceLC, etc.) | [optional] [default to 'CustomerInvoiceLC']
**pdp_flow_service_url** | **str** |  | [optional] 
**pdp_token_url** | **str** |  | [optional] 
**pdp_client_id** | **str** |  | [optional] 
**pdp_client_secret** | **str** |  | [optional] 

## Example

```python
from factpulse.models.submit_cdar_request import SubmitCDARRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitCDARRequest from a JSON string
submit_cdar_request_instance = SubmitCDARRequest.from_json(json)
# print the JSON string representation of the object
print(SubmitCDARRequest.to_json())

# convert the object into a dict
submit_cdar_request_dict = submit_cdar_request_instance.to_dict()
# create an instance of SubmitCDARRequest from a dict
submit_cdar_request_from_dict = SubmitCDARRequest.from_dict(submit_cdar_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


