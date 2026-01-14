# AggregatedPaymentInput

Aggregated payment for B2C (flux 10.4).  Used for B2C payment aggregates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **date** | Payment date | 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**amounts_by_rate** | [**List[PaymentAmountByRate]**](PaymentAmountByRate.md) | Payment amounts by VAT rate | 

## Example

```python
from factpulse.models.aggregated_payment_input import AggregatedPaymentInput

# TODO update the JSON string below
json = "{}"
# create an instance of AggregatedPaymentInput from a JSON string
aggregated_payment_input_instance = AggregatedPaymentInput.from_json(json)
# print the JSON string representation of the object
print(AggregatedPaymentInput.to_json())

# convert the object into a dict
aggregated_payment_input_dict = aggregated_payment_input_instance.to_dict()
# create an instance of AggregatedPaymentInput from a dict
aggregated_payment_input_from_dict = AggregatedPaymentInput.from_dict(aggregated_payment_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


