# ConnectionRouteSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**ConnectionRouteEntrySortDirection**](ConnectionRouteEntrySortDirection.md) |  | [optional] 
**var_property** | [**ConnectionRouteEntrySortBy**](ConnectionRouteEntrySortBy.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connection_route_sort_criteria import ConnectionRouteSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionRouteSortCriteria from a JSON string
connection_route_sort_criteria_instance = ConnectionRouteSortCriteria.from_json(json)
# print the JSON string representation of the object
print(ConnectionRouteSortCriteria.to_json())

# convert the object into a dict
connection_route_sort_criteria_dict = connection_route_sort_criteria_instance.to_dict()
# create an instance of ConnectionRouteSortCriteria from a dict
connection_route_sort_criteria_form_dict = connection_route_sort_criteria.from_dict(connection_route_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


