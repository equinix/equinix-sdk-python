# MetroConnectOrder

Metro Connect Order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_order_number** | **str** | purchase order number | [optional] 
**order_id** | **str** | Order Identification | [optional] 
**customer_reference_id** | **str** | Customer order reference Id | [optional] 
**order_number** | **str** | Order Reference Number | [optional] 
**uuid** | **str** | Equinix-assigned order identifier, this is a derived response attribute | [optional] 

## Example

```python
from equinix.services.fabricv4.models.metro_connect_order import MetroConnectOrder

# TODO update the JSON string below
json = "{}"
# create an instance of MetroConnectOrder from a JSON string
metro_connect_order_instance = MetroConnectOrder.from_json(json)
# print the JSON string representation of the object
print(MetroConnectOrder.to_json())

# convert the object into a dict
metro_connect_order_dict = metro_connect_order_instance.to_dict()
# create an instance of MetroConnectOrder from a dict
metro_connect_order_from_dict = MetroConnectOrder.from_dict(metro_connect_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


