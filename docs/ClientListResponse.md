# ClientListResponse

Paginated client list response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ClientSummary]**](ClientSummary.md) | List of clients | 
**total** | **int** | Total number of clients | 
**page** | **int** | Current page | 
**page_size** | **int** | Page size | 

## Example

```python
from factpulse.models.client_list_response import ClientListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClientListResponse from a JSON string
client_list_response_instance = ClientListResponse.from_json(json)
# print the JSON string representation of the object
print(ClientListResponse.to_json())

# convert the object into a dict
client_list_response_dict = client_list_response_instance.to_dict()
# create an instance of ClientListResponse from a dict
client_list_response_from_dict = ClientListResponse.from_dict(client_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


