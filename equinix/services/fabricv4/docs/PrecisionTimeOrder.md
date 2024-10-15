# PrecisionTimeOrder

Precision Time Order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_order_number** | **str** | Purchase order number | [optional] 
**customer_reference_number** | **str** | Customer reference number | [optional] 
**order_number** | **str** | Order Reference Number | [optional] 

## Example

```python
from equinix.services.fabricv4.models.precision_time_order import PrecisionTimeOrder

# TODO update the JSON string below
json = "{}"
# create an instance of PrecisionTimeOrder from a JSON string
precision_time_order_instance = PrecisionTimeOrder.from_json(json)
# print the JSON string representation of the object
print(PrecisionTimeOrder.to_json())

# convert the object into a dict
precision_time_order_dict = precision_time_order_instance.to_dict()
# create an instance of PrecisionTimeOrder from a dict
precision_time_order_form_dict = precision_time_order.from_dict(precision_time_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


