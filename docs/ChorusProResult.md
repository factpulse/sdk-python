# ChorusProResult

Result of submission to Chorus Pro.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chorus_invoice_id** | **int** | Chorus Pro invoice ID | 
**deposit_flow_number** | **str** |  | [optional] 
**attachment_id** | **int** |  | [optional] 

## Example

```python
from factpulse.models.chorus_pro_result import ChorusProResult

# TODO update the JSON string below
json = "{}"
# create an instance of ChorusProResult from a JSON string
chorus_pro_result_instance = ChorusProResult.from_json(json)
# print the JSON string representation of the object
print(ChorusProResult.to_json())

# convert the object into a dict
chorus_pro_result_dict = chorus_pro_result_instance.to_dict()
# create an instance of ChorusProResult from a dict
chorus_pro_result_from_dict = ChorusProResult.from_dict(chorus_pro_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


