# VirtualConnectionPriceASide


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_point** | [**VirtualConnectionPriceASideAccessPoint**](VirtualConnectionPriceASideAccessPoint.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.virtual_connection_price_a_side import VirtualConnectionPriceASide

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualConnectionPriceASide from a JSON string
virtual_connection_price_a_side_instance = VirtualConnectionPriceASide.from_json(json)
# print the JSON string representation of the object
print(VirtualConnectionPriceASide.to_json())

# convert the object into a dict
virtual_connection_price_a_side_dict = virtual_connection_price_a_side_instance.to_dict()
# create an instance of VirtualConnectionPriceASide from a dict
virtual_connection_price_a_side_from_dict = VirtualConnectionPriceASide.from_dict(virtual_connection_price_a_side_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


