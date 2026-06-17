# IpBlockOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_order_number** | **str** | Purchase order number | [optional] 
**order_number** | **str** | Order Number | [optional] 
**order_line** | **str** | Order Line Number | [optional] 

## Example

```python
from equinix.services.fabricv4.models.ip_block_order_request import IpBlockOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IpBlockOrderRequest from a JSON string
ip_block_order_request_instance = IpBlockOrderRequest.from_json(json)
# print the JSON string representation of the object
print(IpBlockOrderRequest.to_json())

# convert the object into a dict
ip_block_order_request_dict = ip_block_order_request_instance.to_dict()
# create an instance of IpBlockOrderRequest from a dict
ip_block_order_request_from_dict = IpBlockOrderRequest.from_dict(ip_block_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


