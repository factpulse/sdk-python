# ConsulterFactureResponse

Détails d'une facture.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code_retour** | **int** |  | 
**libelle** | **str** |  | 
**identifiant_facture_cpp** | **int** |  | [optional] 
**numero_facture** | **str** |  | [optional] 
**date_facture** | **str** |  | [optional] 
**montant_ttc_total** | **str** |  | [optional] 
**statut_courant** | [**StatutFacture**](StatutFacture.md) |  | [optional] 
**id_structure_cpp_destinataire** | **int** |  | [optional] 
**designation_structure_destinataire** | **str** |  | [optional] 

## Example

```python
from factpulse.models.consulter_facture_response import ConsulterFactureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConsulterFactureResponse from a JSON string
consulter_facture_response_instance = ConsulterFactureResponse.from_json(json)
# print the JSON string representation of the object
print(ConsulterFactureResponse.to_json())

# convert the object into a dict
consulter_facture_response_dict = consulter_facture_response_instance.to_dict()
# create an instance of ConsulterFactureResponse from a dict
consulter_facture_response_from_dict = ConsulterFactureResponse.from_dict(consulter_facture_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


