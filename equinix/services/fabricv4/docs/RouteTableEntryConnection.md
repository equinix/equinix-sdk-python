# RouteTableEntryConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_table_entry_connection import RouteTableEntryConnection

# TODO update the JSON string below
json = "{}"
# create an instance of RouteTableEntryConnection from a JSON string
route_table_entry_connection_instance = RouteTableEntryConnection.from_json(json)
# print the JSON string representation of the object
print(RouteTableEntryConnection.to_json())

# convert the object into a dict
route_table_entry_connection_dict = route_table_entry_connection_instance.to_dict()
# create an instance of RouteTableEntryConnection from a dict
route_table_entry_connection_from_dict = RouteTableEntryConnection.from_dict(route_table_entry_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


