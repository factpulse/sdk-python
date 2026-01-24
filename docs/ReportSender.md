# ReportSender

Report sender information (PA transmitting the report).  In PPF architecture, the sender is typically the PA (Plateforme Agréée) transmitting on behalf of the declarant (issuer).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**siren** | **str** | SIREN or SIRET number of the sender (PA or company) | 
**name** | **str** | Company name | 
**vat_id** | **str** |  | [optional] 

## Example

```python
from factpulse.models.report_sender import ReportSender

# TODO update the JSON string below
json = "{}"
# create an instance of ReportSender from a JSON string
report_sender_instance = ReportSender.from_json(json)
# print the JSON string representation of the object
print(ReportSender.to_json())

# convert the object into a dict
report_sender_dict = report_sender_instance.to_dict()
# create an instance of ReportSender from a dict
report_sender_from_dict = ReportSender.from_dict(report_sender_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


