# IpBlockAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**IpBlockProductType**](IpBlockProductType.md) |  | 
**uuid** | **str** | Unique identifier for the asset | 
**href** | **str** | Resource URL path for the linked resource | 

## Example

```python
from equinix.services.fabricv4.models.ip_block_asset import IpBlockAsset

# TODO update the JSON string below
json = "{}"
# create an instance of IpBlockAsset from a JSON string
ip_block_asset_instance = IpBlockAsset.from_json(json)
# print the JSON string representation of the object
print(IpBlockAsset.to_json())

# convert the object into a dict
ip_block_asset_dict = ip_block_asset_instance.to_dict()
# create an instance of IpBlockAsset from a dict
ip_block_asset_from_dict = IpBlockAsset.from_dict(ip_block_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


