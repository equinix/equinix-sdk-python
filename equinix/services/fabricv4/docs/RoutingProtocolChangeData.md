# RoutingProtocolChangeData

Current state of latest Routing Protocol change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Current outcome of the change flow | [optional] 
**created_by** | **str** | Created by User Key | [optional] 
**created_date_time** | **datetime** | Set when change flow starts | [optional] 
**updated_by** | **str** | Updated by User Key | [optional] 
**updated_date_time** | **datetime** | Set when change object is updated | [optional] 
**information** | **str** | Additional information | [optional] 
**data** | [**RoutingProtocolChangeOperation**](RoutingProtocolChangeOperation.md) |  | [optional] 
**uuid** | **str** | Uniquely identifies a change | 
**type** | [**RoutingProtocolChangeType**](RoutingProtocolChangeType.md) |  | 
**href** | **str** | Routing Protocol Change URI | [optional] 

## Example

```python
from equinix.services.fabricv4.models.routing_protocol_change_data import RoutingProtocolChangeData

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingProtocolChangeData from a JSON string
routing_protocol_change_data_instance = RoutingProtocolChangeData.from_json(json)
# print the JSON string representation of the object
print(RoutingProtocolChangeData.to_json())

# convert the object into a dict
routing_protocol_change_data_dict = routing_protocol_change_data_instance.to_dict()
# create an instance of RoutingProtocolChangeData from a dict
routing_protocol_change_data_form_dict = routing_protocol_change_data.from_dict(routing_protocol_change_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


