# LifecycleEvent

Evenement de cycle de vie d'une facture.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **str** | ID du flux lifecycle | 
**status_code** | **str** | Code statut (200-601) | 
**status_description** | **str** |  | [optional] 
**ack_status** | **str** |  | [optional] 
**at** | **str** |  | [optional] 
**document_id** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**issuer_siren** | **str** |  | [optional] 
**issuer_role** | **str** |  | [optional] 
**reason_code** | **str** |  | [optional] 

## Example

```python
from factpulse.models.lifecycle_event import LifecycleEvent

# TODO update the JSON string below
json = "{}"
# create an instance of LifecycleEvent from a JSON string
lifecycle_event_instance = LifecycleEvent.from_json(json)
# print the JSON string representation of the object
print(LifecycleEvent.to_json())

# convert the object into a dict
lifecycle_event_dict = lifecycle_event_instance.to_dict()
# create an instance of LifecycleEvent from a dict
lifecycle_event_from_dict = LifecycleEvent.from_dict(lifecycle_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


