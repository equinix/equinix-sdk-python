# ConnectionRouteEntrySimpleExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Possible field names to use on filters:  * &#x60;/type&#x60; - Route table entry type  * &#x60;/state&#x60; - Route table entry state  * &#x60;/prefix&#x60; - Route table entry prefix  * &#x60;/nextHop&#x60; - Route table entry nextHop  * &#x60;/*&#x60; - all-category search  | [optional] 
**operator** | **str** | Possible operators to use on filters:  * &#x60;&#x3D;&#x60; - equal  * &#x60;!&#x3D;&#x60; - not equal  * &#x60;&gt;&#x60; - greater than  * &#x60;&gt;&#x3D;&#x60; - greater than or equal to  * &#x60;&lt;&#x60; - less than  * &#x60;&lt;&#x3D;&#x60; - less than or equal to  * &#x60;[NOT] BETWEEN&#x60; - (not) between  * &#x60;[NOT] LIKE&#x60; - (not) like  * &#x60;[NOT] IN&#x60; - (not) in  * &#x60;~*&#x60; - case-insensitive like  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connection_route_entry_simple_expression import ConnectionRouteEntrySimpleExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionRouteEntrySimpleExpression from a JSON string
connection_route_entry_simple_expression_instance = ConnectionRouteEntrySimpleExpression.from_json(json)
# print the JSON string representation of the object
print(ConnectionRouteEntrySimpleExpression.to_json())

# convert the object into a dict
connection_route_entry_simple_expression_dict = connection_route_entry_simple_expression_instance.to_dict()
# create an instance of ConnectionRouteEntrySimpleExpression from a dict
connection_route_entry_simple_expression_from_dict = ConnectionRouteEntrySimpleExpression.from_dict(connection_route_entry_simple_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


