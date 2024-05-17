# MetadataNetwork


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** |  | [optional] 
**href** | **str** |  | [optional] 
**interfaces** | **List[object]** |  | [optional] 
**network** | [**MetadataNetworkNetwork**](MetadataNetworkNetwork.md) |  | [optional] 

## Example

```python
from equinix_metal.models.metadata_network import MetadataNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataNetwork from a JSON string
metadata_network_instance = MetadataNetwork.from_json(json)
# print the JSON string representation of the object
print(MetadataNetwork.to_json())

# convert the object into a dict
metadata_network_dict = metadata_network_instance.to_dict()
# create an instance of MetadataNetwork from a dict
metadata_network_form_dict = metadata_network.from_dict(metadata_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


