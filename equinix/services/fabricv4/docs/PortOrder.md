# PortOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_order** | [**PortOrderPurchaseOrder**](PortOrderPurchaseOrder.md) |  | [optional] 
**order_id** | **str** | Order Identification | [optional] 
**customer_reference_id** | **str** | Customer order reference Id | [optional] 
**order_number** | **str** | Order Reference Number | [optional] 
**uuid** | **str** | Equinix-assigned order identifier | [optional] 
**signature** | [**PortOrderSignature**](PortOrderSignature.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.port_order import PortOrder

# TODO update the JSON string below
json = "{}"
# create an instance of PortOrder from a JSON string
port_order_instance = PortOrder.from_json(json)
# print the JSON string representation of the object
print(PortOrder.to_json())

# convert the object into a dict
port_order_dict = port_order_instance.to_dict()
# create an instance of PortOrder from a dict
port_order_form_dict = port_order.from_dict(port_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


