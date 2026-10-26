# PurchaseOrder

Purchase Order information associated with the account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Purchase Order number. | [optional] 
**amount** | **str** | Purchase Order amount. | [optional] 
**start_date** | **date** | Date the Purchase Order takes effect. | [optional] 
**end_date** | **date** | Date the Purchase Order expires. | [optional] 
**attachment_id** | **str** | Identifier of the uploaded purchase order document. | [optional] 
**type** | [**PurchaseOrderType**](PurchaseOrderType.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.purchase_order import PurchaseOrder

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrder from a JSON string
purchase_order_instance = PurchaseOrder.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrder.to_json())

# convert the object into a dict
purchase_order_dict = purchase_order_instance.to_dict()
# create an instance of PurchaseOrder from a dict
purchase_order_from_dict = PurchaseOrder.from_dict(purchase_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


