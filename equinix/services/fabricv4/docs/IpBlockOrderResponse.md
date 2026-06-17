# IpBlockOrderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Order URI | 
**order_number** | **str** | Order number | 

## Example

```python
from equinix.services.fabricv4.models.ip_block_order_response import IpBlockOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IpBlockOrderResponse from a JSON string
ip_block_order_response_instance = IpBlockOrderResponse.from_json(json)
# print the JSON string representation of the object
print(IpBlockOrderResponse.to_json())

# convert the object into a dict
ip_block_order_response_dict = ip_block_order_response_instance.to_dict()
# create an instance of IpBlockOrderResponse from a dict
ip_block_order_response_from_dict = IpBlockOrderResponse.from_dict(ip_block_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


