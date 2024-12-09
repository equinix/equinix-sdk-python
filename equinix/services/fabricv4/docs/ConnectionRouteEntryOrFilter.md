# ConnectionRouteEntryOrFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_or** | [**List[ConnectionRouteEntrySimpleExpression]**](ConnectionRouteEntrySimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connection_route_entry_or_filter import ConnectionRouteEntryOrFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionRouteEntryOrFilter from a JSON string
connection_route_entry_or_filter_instance = ConnectionRouteEntryOrFilter.from_json(json)
# print the JSON string representation of the object
print(ConnectionRouteEntryOrFilter.to_json())

# convert the object into a dict
connection_route_entry_or_filter_dict = connection_route_entry_or_filter_instance.to_dict()
# create an instance of ConnectionRouteEntryOrFilter from a dict
connection_route_entry_or_filter_form_dict = connection_route_entry_or_filter.from_dict(connection_route_entry_or_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

