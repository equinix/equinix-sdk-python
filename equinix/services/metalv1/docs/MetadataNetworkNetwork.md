# MetadataNetworkNetwork


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bonding** | [**MetadataNetworkNetworkBonding**](MetadataNetworkNetworkBonding.md) |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.metadata_network_network import MetadataNetworkNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataNetworkNetwork from a JSON string
metadata_network_network_instance = MetadataNetworkNetwork.from_json(json)
# print the JSON string representation of the object
print(MetadataNetworkNetwork.to_json())

# convert the object into a dict
metadata_network_network_dict = metadata_network_network_instance.to_dict()
# create an instance of MetadataNetworkNetwork from a dict
metadata_network_network_form_dict = metadata_network_network.from_dict(metadata_network_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


