# Order


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_order_number** | **str** | Purchase order number | [optional] 
**customer_reference_number** | **str** | Customer reference number | [optional] 
**billing_tier** | **str** | Billing tier for connection bandwidth | [optional] 
**order_id** | **str** | Order Identification | [optional] 
**order_number** | **str** | Order Reference Number | [optional] 

## Example

```python
from equinix.services.fabricv4.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print(Order.to_json())

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_from_dict = Order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


