# ConnectionRouteTableEntry

Adv/Rec Route table entry object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RouteTableEntryType**](RouteTableEntryType.md) |  | 
**protocol_type** | [**RouteTableEntryProtocolType**](RouteTableEntryProtocolType.md) |  | [optional] 
**state** | [**ConnectionRouteTableEntryState**](ConnectionRouteTableEntryState.md) |  | 
**age** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**next_hop** | **str** |  | [optional] 
**med** | **int** |  | [optional] 
**local_preference** | **int** |  | [optional] 
**as_path** | **List[str]** |  | [optional] 
**connection** | [**ConnectionRouteTableEntryConnection**](ConnectionRouteTableEntryConnection.md) |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.connection_route_table_entry import ConnectionRouteTableEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionRouteTableEntry from a JSON string
connection_route_table_entry_instance = ConnectionRouteTableEntry.from_json(json)
# print the JSON string representation of the object
print(ConnectionRouteTableEntry.to_json())

# convert the object into a dict
connection_route_table_entry_dict = connection_route_table_entry_instance.to_dict()
# create an instance of ConnectionRouteTableEntry from a dict
connection_route_table_entry_form_dict = connection_route_table_entry.from_dict(connection_route_table_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


