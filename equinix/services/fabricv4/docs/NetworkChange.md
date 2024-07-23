# NetworkChange

Current state of latest network change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Network URI | [optional] [readonly] 
**uuid** | **str** | Uniquely identifies a change | [optional] 
**type** | [**NetworkChangeType**](NetworkChangeType.md) |  | [optional] 
**status** | [**NetworkChangeStatus**](NetworkChangeStatus.md) |  | [optional] 
**created_date_time** | **datetime** | Set when change flow starts | [optional] 
**updated_date_time** | **datetime** | Set when change object is updated | [optional] 
**data** | [**List[NetworkChangeOperation]**](NetworkChangeOperation.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.network_change import NetworkChange

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkChange from a JSON string
network_change_instance = NetworkChange.from_json(json)
# print the JSON string representation of the object
print(NetworkChange.to_json())

# convert the object into a dict
network_change_dict = network_change_instance.to_dict()
# create an instance of NetworkChange from a dict
network_change_form_dict = network_change.from_dict(network_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


