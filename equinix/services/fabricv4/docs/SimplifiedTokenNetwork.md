# SimplifiedTokenNetwork


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | url to entity | [optional] 
**uuid** | **str** | Network Identifier | [optional] 
**type** | [**SimplifiedTokenNetworkType**](SimplifiedTokenNetworkType.md) |  | [optional] 
**name** | **str** | Network Name | [optional] 
**scope** | [**SimplifiedTokenNetworkScope**](SimplifiedTokenNetworkScope.md) |  | [optional] 
**location** | [**SimplifiedLocation**](SimplifiedLocation.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.simplified_token_network import SimplifiedTokenNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedTokenNetwork from a JSON string
simplified_token_network_instance = SimplifiedTokenNetwork.from_json(json)
# print the JSON string representation of the object
print(SimplifiedTokenNetwork.to_json())

# convert the object into a dict
simplified_token_network_dict = simplified_token_network_instance.to_dict()
# create an instance of SimplifiedTokenNetwork from a dict
simplified_token_network_from_dict = SimplifiedTokenNetwork.from_dict(simplified_token_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


