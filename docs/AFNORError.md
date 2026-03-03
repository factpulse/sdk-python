# AFNORError

Error code

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** | Short numerical or alphanumerical code that identifies precisely a unique error. | 
**error_message** | **str** | Contains information on the error. Not intended to be displayed to an end user. For security reasons, a tradeoff between clarity &amp; security shall be found. | [optional] 
**type** | **str** |  | [optional] [default to 'about:blank']
**details** | **str** |  | [optional] 
**instance** | **str** |  | [optional] 

## Example

```python
from factpulse.models.afnor_error import AFNORError

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORError from a JSON string
afnor_error_instance = AFNORError.from_json(json)
# print the JSON string representation of the object
print(AFNORError.to_json())

# convert the object into a dict
afnor_error_dict = afnor_error_instance.to_dict()
# create an instance of AFNORError from a dict
afnor_error_from_dict = AFNORError.from_dict(afnor_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


