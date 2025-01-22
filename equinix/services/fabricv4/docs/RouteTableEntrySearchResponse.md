# RouteTableEntrySearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[RouteTableEntry]**](RouteTableEntry.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_table_entry_search_response import RouteTableEntrySearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RouteTableEntrySearchResponse from a JSON string
route_table_entry_search_response_instance = RouteTableEntrySearchResponse.from_json(json)
# print the JSON string representation of the object
print(RouteTableEntrySearchResponse.to_json())

# convert the object into a dict
route_table_entry_search_response_dict = route_table_entry_search_response_instance.to_dict()
# create an instance of RouteTableEntrySearchResponse from a dict
route_table_entry_search_response_from_dict = RouteTableEntrySearchResponse.from_dict(route_table_entry_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


