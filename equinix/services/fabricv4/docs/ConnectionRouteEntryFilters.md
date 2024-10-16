# ConnectionRouteEntryFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[ConnectionRouteEntryFilter]**](ConnectionRouteEntryFilter.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connection_route_entry_filters import ConnectionRouteEntryFilters

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionRouteEntryFilters from a JSON string
connection_route_entry_filters_instance = ConnectionRouteEntryFilters.from_json(json)
# print the JSON string representation of the object
print(ConnectionRouteEntryFilters.to_json())

# convert the object into a dict
connection_route_entry_filters_dict = connection_route_entry_filters_instance.to_dict()
# create an instance of ConnectionRouteEntryFilters from a dict
connection_route_entry_filters_form_dict = connection_route_entry_filters.from_dict(connection_route_entry_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


