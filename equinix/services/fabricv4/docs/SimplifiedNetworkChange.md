# SimplifiedNetworkChange

Current state of latest network change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Network URI | [optional] [readonly] 
**uuid** | **str** | Uniquely identifies a change | [optional] 
**type** | [**NetworkChangeType**](NetworkChangeType.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.simplified_network_change import SimplifiedNetworkChange

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedNetworkChange from a JSON string
simplified_network_change_instance = SimplifiedNetworkChange.from_json(json)
# print the JSON string representation of the object
print(SimplifiedNetworkChange.to_json())

# convert the object into a dict
simplified_network_change_dict = simplified_network_change_instance.to_dict()
# create an instance of SimplifiedNetworkChange from a dict
simplified_network_change_form_dict = simplified_network_change.from_dict(simplified_network_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


