# AFNORHealthCheckResponse

Response from AFNOR services healthcheck.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_service_ok** | **bool** | Flow Service API status | 
**directory_service_ok** | **bool** | Directory Service API status | 
**message** | **str** | Descriptive status message | 

## Example

```python
from factpulse.models.afnor_health_check_response import AFNORHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AFNORHealthCheckResponse from a JSON string
afnor_health_check_response_instance = AFNORHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(AFNORHealthCheckResponse.to_json())

# convert the object into a dict
afnor_health_check_response_dict = afnor_health_check_response_instance.to_dict()
# create an instance of AFNORHealthCheckResponse from a dict
afnor_health_check_response_from_dict = AFNORHealthCheckResponse.from_dict(afnor_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


