# AFNORAcknowledgement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**AFNORFlowAckStatus**](AFNORFlowAckStatus.md) |  | 
**details** | [**List[AFNORAcknowledgementDetail]**](AFNORAcknowledgementDetail.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_acknowledgement import AFNORAcknowledgement

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORAcknowledgement from a JSON string
afnor_acknowledgement_instance = AFNORAcknowledgement.from_json(json)
# print the JSON string representation of the object
print(AFNORAcknowledgement.to_json())

# convert the object into a dict
afnor_acknowledgement_dict = afnor_acknowledgement_instance.to_dict()
# create an instance of AFNORAcknowledgement from a dict
afnor_acknowledgement_from_dict = AFNORAcknowledgement.from_dict(afnor_acknowledgement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


