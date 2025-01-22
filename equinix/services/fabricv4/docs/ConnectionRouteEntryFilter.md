# ConnectionRouteEntryFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Possible field names to use on filters:  * &#x60;/type&#x60; - Route table entry type  * &#x60;/state&#x60; - Route table entry state  * &#x60;/prefix&#x60; - Route table entry prefix  * &#x60;/nextHop&#x60; - Route table entry nextHop  * &#x60;/*&#x60; - all-category search  | [optional] 
**operator** | **str** | Possible operators to use on filters:  * &#x60;&#x3D;&#x60; - equal  * &#x60;!&#x3D;&#x60; - not equal  * &#x60;&gt;&#x60; - greater than  * &#x60;&gt;&#x3D;&#x60; - greater than or equal to  * &#x60;&lt;&#x60; - less than  * &#x60;&lt;&#x3D;&#x60; - less than or equal to  * &#x60;[NOT] BETWEEN&#x60; - (not) between  * &#x60;[NOT] LIKE&#x60; - (not) like  * &#x60;[NOT] IN&#x60; - (not) in  * &#x60;~*&#x60; - case-insensitive like  | [optional] 
**values** | **List[str]** |  | [optional] 
**var_or** | [**List[ConnectionRouteEntrySimpleExpression]**](ConnectionRouteEntrySimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connection_route_entry_filter import ConnectionRouteEntryFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionRouteEntryFilter from a JSON string
connection_route_entry_filter_instance = ConnectionRouteEntryFilter.from_json(json)
# print the JSON string representation of the object
print(ConnectionRouteEntryFilter.to_json())

# convert the object into a dict
connection_route_entry_filter_dict = connection_route_entry_filter_instance.to_dict()
# create an instance of ConnectionRouteEntryFilter from a dict
connection_route_entry_filter_from_dict = ConnectionRouteEntryFilter.from_dict(connection_route_entry_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


