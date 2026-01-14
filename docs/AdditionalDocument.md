# AdditionalDocument

Additional supporting document (BG-24).  References to external documents or embedded attachments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document reference identifier (BT-122). | 
**type_code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 
**reference_type_code** | **str** |  | [optional] 

## Example

```python
from factpulse.models.additional_document import AdditionalDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalDocument from a JSON string
additional_document_instance = AdditionalDocument.from_json(json)
# print the JSON string representation of the object
print(AdditionalDocument.to_json())

# convert the object into a dict
additional_document_dict = additional_document_instance.to_dict()
# create an instance of AdditionalDocument from a dict
additional_document_from_dict = AdditionalDocument.from_dict(additional_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


