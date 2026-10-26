# OrderResponse

Cross Connect Order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_number** | **str** | Order Number. | [optional] 
**order_line_item_number** | **str** | Order Line Item Number. | [optional] 
**purchase_order** | [**PurchaseOrder**](PurchaseOrder.md) |  | [optional] 
**customer_reference_id** | **str** | Customer Reference Identifier. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.order_response import OrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderResponse from a JSON string
order_response_instance = OrderResponse.from_json(json)
# print the JSON string representation of the object
print(OrderResponse.to_json())

# convert the object into a dict
order_response_dict = order_response_instance.to_dict()
# create an instance of OrderResponse from a dict
order_response_from_dict = OrderResponse.from_dict(order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


