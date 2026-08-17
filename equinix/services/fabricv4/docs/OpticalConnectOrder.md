# OpticalConnectOrder

Ordering and billing reference details for this connection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_order_number** | **str** | Purchase order number reference. | [optional] 
**customer_reference_id** | **str** | Your own reference for this connection. | [optional] 
**order_number** | **str** | Equinix order reference number. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.optical_connect_order import OpticalConnectOrder

# TODO update the JSON string below
json = "{}"
# create an instance of OpticalConnectOrder from a JSON string
optical_connect_order_instance = OpticalConnectOrder.from_json(json)
# print the JSON string representation of the object
print(OpticalConnectOrder.to_json())

# convert the object into a dict
optical_connect_order_dict = optical_connect_order_instance.to_dict()
# create an instance of OpticalConnectOrder from a dict
optical_connect_order_from_dict = OpticalConnectOrder.from_dict(optical_connect_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


