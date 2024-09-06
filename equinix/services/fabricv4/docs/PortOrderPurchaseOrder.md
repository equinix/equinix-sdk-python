# PortOrderPurchaseOrder

purchase order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | purchase order number | [optional] 
**amount** | **str** | purchase order amount | [optional] 
**start_date** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**attachment_id** | **str** |  | [optional] 
**selection_type** | [**PortOrderPurchaseOrderSelectionType**](PortOrderPurchaseOrderSelectionType.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.port_order_purchase_order import PortOrderPurchaseOrder

# TODO update the JSON string below
json = "{}"
# create an instance of PortOrderPurchaseOrder from a JSON string
port_order_purchase_order_instance = PortOrderPurchaseOrder.from_json(json)
# print the JSON string representation of the object
print(PortOrderPurchaseOrder.to_json())

# convert the object into a dict
port_order_purchase_order_dict = port_order_purchase_order_instance.to_dict()
# create an instance of PortOrderPurchaseOrder from a dict
port_order_purchase_order_from_dict = PortOrderPurchaseOrder.from_dict(port_order_purchase_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


