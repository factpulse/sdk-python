# AFNOROAuth2Authentication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_url** | **str** |  | 
**client_id** | **str** |  | 
**client_secret** | **str** |  | 

## Example

```python
from factpulse.models.afnoro_auth2_authentication import AFNOROAuth2Authentication

# TODO update the JSON string below
json = "{}"
# create an instance of AFNOROAuth2Authentication from a JSON string
afnoro_auth2_authentication_instance = AFNOROAuth2Authentication.from_json(json)
# print the JSON string representation of the object
print(AFNOROAuth2Authentication.to_json())

# convert the object into a dict
afnoro_auth2_authentication_dict = afnoro_auth2_authentication_instance.to_dict()
# create an instance of AFNOROAuth2Authentication from a dict
afnoro_auth2_authentication_from_dict = AFNOROAuth2Authentication.from_dict(afnoro_auth2_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


