# AFNORAcknowledgementDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** |  | 
**item** | **str** | Item on which the error refers | 
**reason_code** | [**AFNORReasonCode**](AFNORReasonCode.md) |  | 
**reason_message** | **str** |  | 

## Example

```python
from factpulse.models.afnor_acknowledgement_detail import AFNORAcknowledgementDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORAcknowledgementDetail from a JSON string
afnor_acknowledgement_detail_instance = AFNORAcknowledgementDetail.from_json(json)
# print the JSON string representation of the object
print(AFNORAcknowledgementDetail.to_json())

# convert the object into a dict
afnor_acknowledgement_detail_dict = afnor_acknowledgement_detail_instance.to_dict()
# create an instance of AFNORAcknowledgementDetail from a dict
afnor_acknowledgement_detail_from_dict = AFNORAcknowledgementDetail.from_dict(afnor_acknowledgement_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


