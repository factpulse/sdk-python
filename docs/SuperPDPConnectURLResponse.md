# SuperPDPConnectURLResponse

SuperPDP OAuth authorization URL for a client.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorize_url** | **str** | URL to redirect the end user to in order to connect their SuperPDP account | 

## Example

```python
from factpulse.models.super_pdp_connect_url_response import SuperPDPConnectURLResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SuperPDPConnectURLResponse from a JSON string
super_pdp_connect_url_response_instance = SuperPDPConnectURLResponse.from_json(json)
# print the JSON string representation of the object
print(SuperPDPConnectURLResponse.to_json())

# convert the object into a dict
super_pdp_connect_url_response_dict = super_pdp_connect_url_response_instance.to_dict()
# create an instance of SuperPDPConnectURLResponse from a dict
super_pdp_connect_url_response_from_dict = SuperPDPConnectURLResponse.from_dict(super_pdp_connect_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


