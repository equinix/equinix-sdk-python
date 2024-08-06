# IpBlockPrice

IP Block Product configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Either uuid or rest of attributes are required | [optional] 
**type** | [**IpBlockType**](IpBlockType.md) |  | [optional] 
**prefix_length** | **int** |  | [optional] 
**location** | [**PriceLocation**](PriceLocation.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.ip_block_price import IpBlockPrice

# TODO update the JSON string below
json = "{}"
# create an instance of IpBlockPrice from a JSON string
ip_block_price_instance = IpBlockPrice.from_json(json)
# print the JSON string representation of the object
print(IpBlockPrice.to_json())

# convert the object into a dict
ip_block_price_dict = ip_block_price_instance.to_dict()
# create an instance of IpBlockPrice from a dict
ip_block_price_from_dict = IpBlockPrice.from_dict(ip_block_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


