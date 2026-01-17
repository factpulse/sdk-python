# CreateCDARRequest

Requête de création d'un message CDAR.

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

## Example

```python
from factpulse.models.create_cdar_request import CreateCDARRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCDARRequest from a JSON string
create_cdar_request_instance = CreateCDARRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCDARRequest.to_json())

# convert the object into a dict
create_cdar_request_dict = create_cdar_request_instance.to_dict()
# create an instance of CreateCDARRequest from a dict
create_cdar_request_from_dict = CreateCDARRequest.from_dict(create_cdar_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


