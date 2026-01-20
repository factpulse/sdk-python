# ClientSummary

Client list view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **UUID** | Unique client identifier | 
**name** | **str** | Client name | 
**siret** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_active** | **bool** | Whether the client is active | 
**has_config_pdp** | **bool** | Whether PDP config exists | 
**pdp_is_active** | **bool** |  | [optional] 
**pdp_is_mock** | **bool** |  | [optional] 
**has_config_chorus** | **bool** | Whether Chorus Pro config exists | 
**created_at** | **datetime** | Creation date | 
**updated_at** | **datetime** | Last update date | 

## Example

```python
from factpulse.models.client_summary import ClientSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ClientSummary from a JSON string
client_summary_instance = ClientSummary.from_json(json)
# print the JSON string representation of the object
print(ClientSummary.to_json())

# convert the object into a dict
client_summary_dict = client_summary_instance.to_dict()
# create an instance of ClientSummary from a dict
client_summary_from_dict = ClientSummary.from_dict(client_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


