# PaymentCard

Payment card information (BG-18).  Used when payment is made by payment card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_id** | **str** |  | [optional] 
**cardholder_name** | **str** |  | [optional] 

## Example

```python
from factpulse.models.payment_card import PaymentCard

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCard from a JSON string
payment_card_instance = PaymentCard.from_json(json)
# print the JSON string representation of the object
print(PaymentCard.to_json())

# convert the object into a dict
payment_card_dict = payment_card_instance.to_dict()
# create an instance of PaymentCard from a dict
payment_card_from_dict = PaymentCard.from_dict(payment_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


