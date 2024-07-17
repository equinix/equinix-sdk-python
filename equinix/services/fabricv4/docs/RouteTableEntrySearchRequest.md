# RouteTableEntrySearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**RouteTableEntryFilters**](RouteTableEntryFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[RouteTableEntrySortCriteria]**](RouteTableEntrySortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_table_entry_search_request import RouteTableEntrySearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RouteTableEntrySearchRequest from a JSON string
route_table_entry_search_request_instance = RouteTableEntrySearchRequest.from_json(json)
# print the JSON string representation of the object
print(RouteTableEntrySearchRequest.to_json())

# convert the object into a dict
route_table_entry_search_request_dict = route_table_entry_search_request_instance.to_dict()
# create an instance of RouteTableEntrySearchRequest from a dict
route_table_entry_search_request_form_dict = route_table_entry_search_request.from_dict(route_table_entry_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


