# RoutingProtocolProject

The Routing Protocol's project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Uniquely identifies a project | 

## Example

```python
from equinix.services.fabricv4.models.routing_protocol_project import RoutingProtocolProject

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingProtocolProject from a JSON string
routing_protocol_project_instance = RoutingProtocolProject.from_json(json)
# print the JSON string representation of the object
print(RoutingProtocolProject.to_json())

# convert the object into a dict
routing_protocol_project_dict = routing_protocol_project_instance.to_dict()
# create an instance of RoutingProtocolProject from a dict
routing_protocol_project_from_dict = RoutingProtocolProject.from_dict(routing_protocol_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


