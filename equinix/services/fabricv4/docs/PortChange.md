# PortChange

Current state of latest port change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Uniquely identifies a change | [optional] 
**type** | [**PortChangeType**](PortChangeType.md) |  | [optional] 
**status** | [**PortChangeStatus**](PortChangeStatus.md) |  | [optional] 
**information** | **str** | Additional information | [optional] 
**data** | [**PortChangeOperation**](PortChangeOperation.md) |  | [optional] 
**created_date_time** | **datetime** | Set when change flow starts | [optional] 
**updated_date_time** | **datetime** | Set when change object is updated | [optional] 

## Example

```python
from equinix.services.fabricv4.models.port_change import PortChange

# TODO update the JSON string below
json = "{}"
# create an instance of PortChange from a JSON string
port_change_instance = PortChange.from_json(json)
# print the JSON string representation of the object
print(PortChange.to_json())

# convert the object into a dict
port_change_dict = port_change_instance.to_dict()
# create an instance of PortChange from a dict
port_change_from_dict = PortChange.from_dict(port_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


