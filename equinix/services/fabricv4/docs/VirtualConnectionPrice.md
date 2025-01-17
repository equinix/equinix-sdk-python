# VirtualConnectionPrice

Virtual Connection Product configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Either uuid or rest of attributes are required | [optional] 
**type** | [**VirtualConnectionPriceConnectionType**](VirtualConnectionPriceConnectionType.md) |  | [optional] 
**bandwidth** | **int** |  | [optional] 
**a_side** | [**VirtualConnectionPriceASide**](VirtualConnectionPriceASide.md) |  | [optional] 
**z_side** | [**VirtualConnectionPriceZSide**](VirtualConnectionPriceZSide.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.virtual_connection_price import VirtualConnectionPrice

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualConnectionPrice from a JSON string
virtual_connection_price_instance = VirtualConnectionPrice.from_json(json)
# print the JSON string representation of the object
print(VirtualConnectionPrice.to_json())

# convert the object into a dict
virtual_connection_price_dict = virtual_connection_price_instance.to_dict()
# create an instance of VirtualConnectionPrice from a dict
virtual_connection_price_from_dict = VirtualConnectionPrice.from_dict(virtual_connection_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


