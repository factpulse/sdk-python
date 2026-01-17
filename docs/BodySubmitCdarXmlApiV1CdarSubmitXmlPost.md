# BodySubmitCdarXmlApiV1CdarSubmitXmlPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**SubmitCDARXMLRequest**](SubmitCDARXMLRequest.md) |  | 
**pdp_credentials** | [**PDPCredentials**](PDPCredentials.md) |  | [optional] 

## Example

```python
from factpulse.models.body_submit_cdar_xml_api_v1_cdar_submit_xml_post import BodySubmitCdarXmlApiV1CdarSubmitXmlPost

# TODO update the JSON string below
json = "{}"
# create an instance of BodySubmitCdarXmlApiV1CdarSubmitXmlPost from a JSON string
body_submit_cdar_xml_api_v1_cdar_submit_xml_post_instance = BodySubmitCdarXmlApiV1CdarSubmitXmlPost.from_json(json)
# print the JSON string representation of the object
print(BodySubmitCdarXmlApiV1CdarSubmitXmlPost.to_json())

# convert the object into a dict
body_submit_cdar_xml_api_v1_cdar_submit_xml_post_dict = body_submit_cdar_xml_api_v1_cdar_submit_xml_post_instance.to_dict()
# create an instance of BodySubmitCdarXmlApiV1CdarSubmitXmlPost from a dict
body_submit_cdar_xml_api_v1_cdar_submit_xml_post_from_dict = BodySubmitCdarXmlApiV1CdarSubmitXmlPost.from_dict(body_submit_cdar_xml_api_v1_cdar_submit_xml_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


