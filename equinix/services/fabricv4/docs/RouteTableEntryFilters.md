# RouteTableEntryFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[RouteTableEntryFilter]**](RouteTableEntryFilter.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_table_entry_filters import RouteTableEntryFilters

# TODO update the JSON string below
json = "{}"
# create an instance of RouteTableEntryFilters from a JSON string
route_table_entry_filters_instance = RouteTableEntryFilters.from_json(json)
# print the JSON string representation of the object
print(RouteTableEntryFilters.to_json())

# convert the object into a dict
route_table_entry_filters_dict = route_table_entry_filters_instance.to_dict()
# create an instance of RouteTableEntryFilters from a dict
route_table_entry_filters_from_dict = RouteTableEntryFilters.from_dict(route_table_entry_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


