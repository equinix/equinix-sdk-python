# OpticalConnectPrice

Optical Metro Connect Port Product configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Optical Connect type. | [optional] 
**bandwidth** | **int** | Bandwidth in Mbps | [optional] 
**path_type** | [**OpticalConnectPricePathType**](OpticalConnectPricePathType.md) |  | [optional] 
**connection_destination_type** | [**OpticalConnectConnectionDestinationType**](OpticalConnectConnectionDestinationType.md) |  | [optional] 
**a_side** | [**OpticalConnectPriceASide**](OpticalConnectPriceASide.md) |  | [optional] 
**z_side** | [**OpticalConnectPriceZSide**](OpticalConnectPriceZSide.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.optical_connect_price import OpticalConnectPrice

# TODO update the JSON string below
json = "{}"
# create an instance of OpticalConnectPrice from a JSON string
optical_connect_price_instance = OpticalConnectPrice.from_json(json)
# print the JSON string representation of the object
print(OpticalConnectPrice.to_json())

# convert the object into a dict
optical_connect_price_dict = optical_connect_price_instance.to_dict()
# create an instance of OpticalConnectPrice from a dict
optical_connect_price_from_dict = OpticalConnectPrice.from_dict(optical_connect_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


