# SubmitCDARXMLRequest

Requête de soumission d'un XML CDAR pré-généré.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xml** | **str** | XML CDAR à soumettre | 
**flow_type** | **str** | Type de flux AFNOR | [optional] [default to 'CustomerInvoiceLC']
**filename** | **str** |  | [optional] 

## Example

```python
from factpulse.models.submit_cdarxml_request import SubmitCDARXMLRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitCDARXMLRequest from a JSON string
submit_cdarxml_request_instance = SubmitCDARXMLRequest.from_json(json)
# print the JSON string representation of the object
print(SubmitCDARXMLRequest.to_json())

# convert the object into a dict
submit_cdarxml_request_dict = submit_cdarxml_request_instance.to_dict()
# create an instance of SubmitCDARXMLRequest from a dict
submit_cdarxml_request_from_dict = SubmitCDARXMLRequest.from_dict(submit_cdarxml_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


