# ConvertPendingInputResponse

Reponse donnees manquantes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] [default to 'pending_input']
**conversion_id** | **str** |  | 
**message** | **str** |  | [optional] [default to 'Donnees manquantes requises pour la conformite']
**extraction** | [**ExtractionInfo**](ExtractionInfo.md) |  | 
**extracted_data** | **Dict[str, object]** | Donnees extraites par OCR au format FacturXInvoice | 
**missing_fields** | [**List[MissingField]**](MissingField.md) |  | 
**resume_url** | **str** |  | 
**expires_at** | **datetime** |  | 

## Example

```python
from factpulse.models.convert_pending_input_response import ConvertPendingInputResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertPendingInputResponse from a JSON string
convert_pending_input_response_instance = ConvertPendingInputResponse.from_json(json)
# print the JSON string representation of the object
print(ConvertPendingInputResponse.to_json())

# convert the object into a dict
convert_pending_input_response_dict = convert_pending_input_response_instance.to_dict()
# create an instance of ConvertPendingInputResponse from a dict
convert_pending_input_response_from_dict = ConvertPendingInputResponse.from_dict(convert_pending_input_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


