# VirtualConnectionPriceASideAccessPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**type** | [**VirtualConnectionPriceAccessPointType**](VirtualConnectionPriceAccessPointType.md) |  | [optional] 
**location** | [**PriceLocation**](PriceLocation.md) |  | [optional] 
**port** | [**VirtualConnectionPriceASideAccessPointPort**](VirtualConnectionPriceASideAccessPointPort.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.virtual_connection_price_a_side_access_point import VirtualConnectionPriceASideAccessPoint

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualConnectionPriceASideAccessPoint from a JSON string
virtual_connection_price_a_side_access_point_instance = VirtualConnectionPriceASideAccessPoint.from_json(json)
# print the JSON string representation of the object
print(VirtualConnectionPriceASideAccessPoint.to_json())

# convert the object into a dict
virtual_connection_price_a_side_access_point_dict = virtual_connection_price_a_side_access_point_instance.to_dict()
# create an instance of VirtualConnectionPriceASideAccessPoint from a dict
virtual_connection_price_a_side_access_point_from_dict = VirtualConnectionPriceASideAccessPoint.from_dict(virtual_connection_price_a_side_access_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


