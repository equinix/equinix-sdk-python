# VirtualConnectionPriceZSideAccessPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**type** | [**VirtualConnectionPriceAccessPointType**](VirtualConnectionPriceAccessPointType.md) |  | [optional] 
**location** | [**PriceLocation**](PriceLocation.md) |  | [optional] 
**port** | [**VirtualConnectionPriceASideAccessPointPort**](VirtualConnectionPriceASideAccessPointPort.md) |  | [optional] 
**profile** | [**VirtualConnectionPriceZSideAccessPointProfile**](VirtualConnectionPriceZSideAccessPointProfile.md) |  | [optional] 
**bridge** | [**VirtualConnectionPriceZSideAccessPointBridge**](VirtualConnectionPriceZSideAccessPointBridge.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.virtual_connection_price_z_side_access_point import VirtualConnectionPriceZSideAccessPoint

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualConnectionPriceZSideAccessPoint from a JSON string
virtual_connection_price_z_side_access_point_instance = VirtualConnectionPriceZSideAccessPoint.from_json(json)
# print the JSON string representation of the object
print(VirtualConnectionPriceZSideAccessPoint.to_json())

# convert the object into a dict
virtual_connection_price_z_side_access_point_dict = virtual_connection_price_z_side_access_point_instance.to_dict()
# create an instance of VirtualConnectionPriceZSideAccessPoint from a dict
virtual_connection_price_z_side_access_point_from_dict = VirtualConnectionPriceZSideAccessPoint.from_dict(virtual_connection_price_z_side_access_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


