# SupplementaryAttachment

Represents a supplementary attachment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Attachment description | 
**id** | **int** | Attachment ID | 
**link_id** | **int** | Link ID | 
**invoice_line_number** | **int** | Invoice line number | 
**type** | **str** | Attachment type | 

## Example

```python
from factpulse.models.supplementary_attachment import SupplementaryAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of SupplementaryAttachment from a JSON string
supplementary_attachment_instance = SupplementaryAttachment.from_json(json)
# print the JSON string representation of the object
print(SupplementaryAttachment.to_json())

# convert the object into a dict
supplementary_attachment_dict = supplementary_attachment_instance.to_dict()
# create an instance of SupplementaryAttachment from a dict
supplementary_attachment_from_dict = SupplementaryAttachment.from_dict(supplementary_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


