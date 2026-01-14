# AggregatedTransactionInput

Aggregated transaction for B2C reporting (flux 10.3).  Represents daily aggregation by category (TLB1, TPS1, etc.). Each occurrence corresponds to one day + one currency + one category.  Source: Annexe 6 v1.9, bloc TG-31 \"Transactions\"

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Transaction date (TT-77) | 
**category_code** | [**TransactionCategory**](TransactionCategory.md) | Transaction category code (TT-81). Use TLB1 for goods, TPS1 for services. | 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**tax_exclusive_amount** | [**Taxexclusiveamount**](Taxexclusiveamount.md) |  | 
**tax_amount** | [**Taxamount**](Taxamount.md) |  | 
**tax_breakdown** | [**List[TaxBreakdownInput]**](TaxBreakdownInput.md) | VAT breakdown by rate | 
**transaction_count** | **int** |  | [optional] 
**tax_due_type** | [**TaxDueDateType**](TaxDueDateType.md) |  | [optional] 

## Example

```python
from factpulse.models.aggregated_transaction_input import AggregatedTransactionInput

# TODO update the JSON string below
json = "{}"
# create an instance of AggregatedTransactionInput from a JSON string
aggregated_transaction_input_instance = AggregatedTransactionInput.from_json(json)
# print the JSON string representation of the object
print(AggregatedTransactionInput.to_json())

# convert the object into a dict
aggregated_transaction_input_dict = aggregated_transaction_input_instance.to_dict()
# create an instance of AggregatedTransactionInput from a dict
aggregated_transaction_input_from_dict = AggregatedTransactionInput.from_dict(aggregated_transaction_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


