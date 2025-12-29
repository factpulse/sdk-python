# ConvertSuccessResponse

Reponse succes de conversion.  Le champ `invoice` contient les donnees de la facture au format FacturXInvoice (cf. facture_electronique.models.FacturXInvoice). Ce modele est le meme que celui utilise pour la generation Factur-X, garantissant une coherence totale.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Statut de la conversion | [optional] [default to 'success']
**conversion_id** | **str** | Identifiant unique de conversion | 
**document_type** | [**DocumentTypeInfo**](DocumentTypeInfo.md) |  | 
**invoice** | **Dict[str, object]** | Donnees facture au format FacturXInvoice (cf. models.py) | 
**extraction** | [**ExtractionInfo**](ExtractionInfo.md) |  | 
**validation** | [**ValidationInfo**](ValidationInfo.md) |  | 
**files** | [**FilesInfo**](FilesInfo.md) |  | 
**processing_time_ms** | **int** | Temps de traitement en ms | 
**pdf_regenerated** | **bool** | True si le PDF a ete regenere (source non exploitable) | [optional] [default to False]
**pdf_regenerated_reason** | **str** |  | [optional] 

## Example

```python
from factpulse.models.convert_success_response import ConvertSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertSuccessResponse from a JSON string
convert_success_response_instance = ConvertSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(ConvertSuccessResponse.to_json())

# convert the object into a dict
convert_success_response_dict = convert_success_response_instance.to_dict()
# create an instance of ConvertSuccessResponse from a dict
convert_success_response_from_dict = ConvertSuccessResponse.from_dict(convert_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


