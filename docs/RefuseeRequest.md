# RefuseeRequest

Requête simplifiée pour soumettre un statut REFUSÉE (210).  Statut obligatoire PPF - Le destinataire refuse la facture. Un code motif est OBLIGATOIRE (BR-FR-CDV-15).  Codes motif autorisés (BR-FR-CDV-CL-09_MDT-113_210): - TX_TVA_ERR: Taux de TVA erroné - MONTANTTOTAL_ERR: Montant total erroné - CALCUL_ERR: Erreur de calcul - NON_CONFORME: Non conforme - DOUBLON: Doublon - DEST_ERR: Destinataire erroné - TRANSAC_INC: Transaction incomplète - EMMET_INC: Émetteur inconnu - CONTRAT_TERM: Contrat terminé - DOUBLE_FACT: Double facturation - CMD_ERR: Commande erronée - ADR_ERR: Adresse erronée - REF_CT_ABSENT: Référence contrat absente

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Identifiant de la facture (BT-1) | 
**invoice_issue_date** | **date** | Date d&#39;émission de la facture (YYYY-MM-DD) | 
**sender_siren** | **str** |  | [optional] 
**flow_type** | **str** | Type de flux: SupplierInvoiceLC (acheteur) ou CustomerInvoiceLC (vendeur) | [optional] [default to 'SupplierInvoiceLC']
**pdp_flow_service_url** | **str** |  | [optional] 
**pdp_token_url** | **str** |  | [optional] 
**pdp_client_id** | **str** |  | [optional] 
**pdp_client_secret** | **str** |  | [optional] 
**reason_code** | **str** | Code motif du refus (obligatoire). Valeurs autorisées: TX_TVA_ERR, MONTANTTOTAL_ERR, CALCUL_ERR, NON_CONFORME, DOUBLON, DEST_ERR, TRANSAC_INC, EMMET_INC, CONTRAT_TERM, DOUBLE_FACT, CMD_ERR, ADR_ERR, REF_CT_ABSENT | 
**reason_text** | **str** |  | [optional] 

## Example

```python
from factpulse.models.refusee_request import RefuseeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RefuseeRequest from a JSON string
refusee_request_instance = RefuseeRequest.from_json(json)
# print the JSON string representation of the object
print(RefuseeRequest.to_json())

# convert the object into a dict
refusee_request_dict = refusee_request_instance.to_dict()
# create an instance of RefuseeRequest from a dict
refusee_request_from_dict = RefuseeRequest.from_dict(refusee_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


