# AFNORDestination

Specific configuration for AFNOR PDP destination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'afnor']
**credentials** | [**AFNORCredentials**](AFNORCredentials.md) |  | [optional] 
**flow_syntax** | [**FlowSyntax**](FlowSyntax.md) | Flow syntax (AFNOR XP Z12-013) | [optional] 
**tracking_id** | **str** |  | [optional] 
**processing_rule** | [**ProcessingRule**](ProcessingRule.md) |  | [optional] 

## Example

```python
from factpulse.models.afnor_destination import AFNORDestination

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORDestination from a JSON string
afnor_destination_instance = AFNORDestination.from_json(json)
# print the JSON string representation of the object
print(AFNORDestination.to_json())

# convert the object into a dict
afnor_destination_dict = afnor_destination_instance.to_dict()
# create an instance of AFNORDestination from a dict
afnor_destination_from_dict = AFNORDestination.from_dict(afnor_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


