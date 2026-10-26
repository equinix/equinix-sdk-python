# ExchangeServiceOrder

Ordering and billing reference details for this Exchange Service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_order_number** | **str** | Purchase order number reference. | [optional] 
**order_id** | **str** | Equinix-assigned order identifier. | [optional] [readonly] 
**customer_reference_id** | **str** | Your own reference for this Exchange Service. | [optional] 
**order_number** | **str** | Equinix order reference number. | [optional] 
**order_line_item_number** | **str** | Order Reference Number for Sales Assisted Order | [optional] [readonly] 
**domain_order_number** | **str** | product domain Order Number for Sales Assisted Order | [optional] [readonly] 
**uuid** | **str** | Equinix-assigned order identifier, this is a derived response attribute | [optional] [readonly] 

## Example

```python
from equinix.services.fabricv4.models.exchange_service_order import ExchangeServiceOrder

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeServiceOrder from a JSON string
exchange_service_order_instance = ExchangeServiceOrder.from_json(json)
# print the JSON string representation of the object
print(ExchangeServiceOrder.to_json())

# convert the object into a dict
exchange_service_order_dict = exchange_service_order_instance.to_dict()
# create an instance of ExchangeServiceOrder from a dict
exchange_service_order_from_dict = ExchangeServiceOrder.from_dict(exchange_service_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


