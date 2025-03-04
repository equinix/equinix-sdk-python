# RouteTableEntry

Route table entry object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RouteTableEntryType**](RouteTableEntryType.md) |  | 
**protocol_type** | [**RouteTableEntryProtocolType**](RouteTableEntryProtocolType.md) |  | [optional] 
**state** | [**RouteTableEntryState**](RouteTableEntryState.md) |  | 
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
from equinix.services.fabricv4.models.route_table_entry import RouteTableEntry

# TODO update the JSON string below
json = "{}"
# create an instance of RouteTableEntry from a JSON string
route_table_entry_instance = RouteTableEntry.from_json(json)
# print the JSON string representation of the object
print(RouteTableEntry.to_json())

# convert the object into a dict
route_table_entry_dict = route_table_entry_instance.to_dict()
# create an instance of RouteTableEntry from a dict
route_table_entry_from_dict = RouteTableEntry.from_dict(route_table_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


