# RouteTableEntryOrFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_or** | [**List[RouteTableEntrySimpleExpression]**](RouteTableEntrySimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_table_entry_or_filter import RouteTableEntryOrFilter

# TODO update the JSON string below
json = "{}"
# create an instance of RouteTableEntryOrFilter from a JSON string
route_table_entry_or_filter_instance = RouteTableEntryOrFilter.from_json(json)
# print the JSON string representation of the object
print(RouteTableEntryOrFilter.to_json())

# convert the object into a dict
route_table_entry_or_filter_dict = route_table_entry_or_filter_instance.to_dict()
# create an instance of RouteTableEntryOrFilter from a dict
route_table_entry_or_filter_form_dict = route_table_entry_or_filter.from_dict(route_table_entry_or_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


