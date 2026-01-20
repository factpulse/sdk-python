# PaymentAmountByRate

Payment amount for a specific VAT rate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate** | [**Rate**](Rate.md) |  | 
**amount** | [**Amount1**](Amount1.md) |  | 

## Example

```python
from factpulse.models.payment_amount_by_rate import PaymentAmountByRate

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAmountByRate from a JSON string
payment_amount_by_rate_instance = PaymentAmountByRate.from_json(json)
# print the JSON string representation of the object
print(PaymentAmountByRate.to_json())

# convert the object into a dict
payment_amount_by_rate_dict = payment_amount_by_rate_instance.to_dict()
# create an instance of PaymentAmountByRate from a dict
payment_amount_by_rate_from_dict = PaymentAmountByRate.from_dict(payment_amount_by_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


