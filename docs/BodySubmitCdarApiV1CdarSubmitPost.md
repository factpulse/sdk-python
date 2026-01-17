# BodySubmitCdarApiV1CdarSubmitPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**SubmitCDARRequest**](SubmitCDARRequest.md) |  | 
**pdp_credentials** | [**PDPCredentials**](PDPCredentials.md) |  | [optional] 

## Example

```python
from factpulse.models.body_submit_cdar_api_v1_cdar_submit_post import BodySubmitCdarApiV1CdarSubmitPost

# TODO update the JSON string below
json = "{}"
# create an instance of BodySubmitCdarApiV1CdarSubmitPost from a JSON string
body_submit_cdar_api_v1_cdar_submit_post_instance = BodySubmitCdarApiV1CdarSubmitPost.from_json(json)
# print the JSON string representation of the object
print(BodySubmitCdarApiV1CdarSubmitPost.to_json())

# convert the object into a dict
body_submit_cdar_api_v1_cdar_submit_post_dict = body_submit_cdar_api_v1_cdar_submit_post_instance.to_dict()
# create an instance of BodySubmitCdarApiV1CdarSubmitPost from a dict
body_submit_cdar_api_v1_cdar_submit_post_from_dict = BodySubmitCdarApiV1CdarSubmitPost.from_dict(body_submit_cdar_api_v1_cdar_submit_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


