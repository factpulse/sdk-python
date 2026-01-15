# DocumentTypeInfo

Informations sur le type de document detecte.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Code UNTDID 1001 | 
**label** | **str** | Libelle (Facture, Avoir, etc.) | 
**detected_as** | **str** | Classification interne | 

## Example

```python
from factpulse.models.document_type_info import DocumentTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTypeInfo from a JSON string
document_type_info_instance = DocumentTypeInfo.from_json(json)
# print the JSON string representation of the object
print(DocumentTypeInfo.to_json())

# convert the object into a dict
document_type_info_dict = document_type_info_instance.to_dict()
# create an instance of DocumentTypeInfo from a dict
document_type_info_from_dict = DocumentTypeInfo.from_dict(document_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


