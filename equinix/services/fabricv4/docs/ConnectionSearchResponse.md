# ConnectionSearchResponse

List of connections

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**sort** | [**List[SortCriteriaResponse]**](SortCriteriaResponse.md) |  | [optional] 
**data** | [**List[Connection]**](Connection.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connection_search_response import ConnectionSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionSearchResponse from a JSON string
connection_search_response_instance = ConnectionSearchResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectionSearchResponse.to_json())

# convert the object into a dict
connection_search_response_dict = connection_search_response_instance.to_dict()
# create an instance of ConnectionSearchResponse from a dict
connection_search_response_form_dict = connection_search_response.from_dict(connection_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


