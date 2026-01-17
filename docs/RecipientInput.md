# RecipientInput

Destinataire du message CDAR.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**siren** | **str** |  | [optional] 
**siret** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**role** | **str** | Code rôle (BY, SE, WK, etc.) | [optional] [default to 'BY']
**email** | **str** |  | [optional] 

## Example

```python
from factpulse.models.recipient_input import RecipientInput

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientInput from a JSON string
recipient_input_instance = RecipientInput.from_json(json)
# print the JSON string representation of the object
print(RecipientInput.to_json())

# convert the object into a dict
recipient_input_dict = recipient_input_instance.to_dict()
# create an instance of RecipientInput from a dict
recipient_input_from_dict = RecipientInput.from_dict(recipient_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


