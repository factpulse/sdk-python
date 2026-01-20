# ClientDetail

Detailed client view (same fields for now).

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
from factpulse.models.client_detail import ClientDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ClientDetail from a JSON string
client_detail_instance = ClientDetail.from_json(json)
# print the JSON string representation of the object
print(ClientDetail.to_json())

# convert the object into a dict
client_detail_dict = client_detail_instance.to_dict()
# create an instance of ClientDetail from a dict
client_detail_from_dict = ClientDetail.from_dict(client_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


