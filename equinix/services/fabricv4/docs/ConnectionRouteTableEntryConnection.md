# ConnectionRouteTableEntryConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connection_route_table_entry_connection import ConnectionRouteTableEntryConnection

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionRouteTableEntryConnection from a JSON string
connection_route_table_entry_connection_instance = ConnectionRouteTableEntryConnection.from_json(json)
# print the JSON string representation of the object
print(ConnectionRouteTableEntryConnection.to_json())

# convert the object into a dict
connection_route_table_entry_connection_dict = connection_route_table_entry_connection_instance.to_dict()
# create an instance of ConnectionRouteTableEntryConnection from a dict
connection_route_table_entry_connection_from_dict = ConnectionRouteTableEntryConnection.from_dict(connection_route_table_entry_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


