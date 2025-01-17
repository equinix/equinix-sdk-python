# ConnectionRouteTableEntrySearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[ConnectionRouteTableEntry]**](ConnectionRouteTableEntry.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connection_route_table_entry_search_response import ConnectionRouteTableEntrySearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionRouteTableEntrySearchResponse from a JSON string
connection_route_table_entry_search_response_instance = ConnectionRouteTableEntrySearchResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectionRouteTableEntrySearchResponse.to_json())

# convert the object into a dict
connection_route_table_entry_search_response_dict = connection_route_table_entry_search_response_instance.to_dict()
# create an instance of ConnectionRouteTableEntrySearchResponse from a dict
connection_route_table_entry_search_response_from_dict = ConnectionRouteTableEntrySearchResponse.from_dict(connection_route_table_entry_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


