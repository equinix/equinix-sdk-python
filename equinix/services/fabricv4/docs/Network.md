# Network

Network specification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**NetworkType**](NetworkType.md) |  | 
**name** | **str** | Customer-provided network name | 
**scope** | [**NetworkScope**](NetworkScope.md) |  | 
**location** | [**SimplifiedLocation**](SimplifiedLocation.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**notifications** | [**List[SimplifiedNotification]**](SimplifiedNotification.md) | Preferences for notifications on network configuration or status changes | 
**href** | **str** | Network URI | [readonly] 
**uuid** | **str** | Equinix-assigned network identifier | 
**state** | [**NetworkState**](NetworkState.md) |  | 
**connections_count** | **float** | number of connections created on the network | [optional] 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | [optional] 
**change** | [**SimplifiedNetworkChange**](SimplifiedNetworkChange.md) |  | [optional] 
**operation** | [**NetworkOperation**](NetworkOperation.md) |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | 
**links** | [**List[Link]**](Link.md) | Network sub-resources links | [optional] [readonly] 

## Example

```python
from equinix.services.fabricv4.models.network import Network

# TODO update the JSON string below
json = "{}"
# create an instance of Network from a JSON string
network_instance = Network.from_json(json)
# print the JSON string representation of the object
print(Network.to_json())

# convert the object into a dict
network_dict = network_instance.to_dict()
# create an instance of Network from a dict
network_form_dict = network.from_dict(network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


