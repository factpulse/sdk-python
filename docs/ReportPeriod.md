# ReportPeriod

Reporting period.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | Period start date (YYYY-MM-DD) | 
**end_date** | **date** | Period end date (YYYY-MM-DD) | 

## Example

```python
from factpulse.models.report_period import ReportPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of ReportPeriod from a JSON string
report_period_instance = ReportPeriod.from_json(json)
# print the JSON string representation of the object
print(ReportPeriod.to_json())

# convert the object into a dict
report_period_dict = report_period_instance.to_dict()
# create an instance of ReportPeriod from a dict
report_period_from_dict = ReportPeriod.from_dict(report_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


