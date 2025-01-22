# SimplifiedNetwork

Network specification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Network URI | [optional] [readonly] 
**uuid** | **str** | Equinix-assigned network identifier | 
**name** | **str** | Customer-assigned network name | [optional] 
**state** | [**NetworkState**](NetworkState.md) |  | [optional] 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | [optional] 
**change** | [**SimplifiedNetworkChange**](SimplifiedNetworkChange.md) |  | [optional] 
**operation** | [**NetworkOperation**](NetworkOperation.md) |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) | Network sub-resources links | [optional] [readonly] 
**type** | [**NetworkType**](NetworkType.md) |  | [optional] 
**scope** | [**NetworkScope**](NetworkScope.md) |  | [optional] 
**location** | [**SimplifiedLocation**](SimplifiedLocation.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.simplified_network import SimplifiedNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedNetwork from a JSON string
simplified_network_instance = SimplifiedNetwork.from_json(json)
# print the JSON string representation of the object
print(SimplifiedNetwork.to_json())

# convert the object into a dict
simplified_network_dict = simplified_network_instance.to_dict()
# create an instance of SimplifiedNetwork from a dict
simplified_network_from_dict = SimplifiedNetwork.from_dict(simplified_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


