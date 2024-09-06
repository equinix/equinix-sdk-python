# PortV4SearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**PortExpression**](PortExpression.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[PortSortCriteria]**](PortSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.port_v4_search_request import PortV4SearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PortV4SearchRequest from a JSON string
port_v4_search_request_instance = PortV4SearchRequest.from_json(json)
# print the JSON string representation of the object
print(PortV4SearchRequest.to_json())

# convert the object into a dict
port_v4_search_request_dict = port_v4_search_request_instance.to_dict()
# create an instance of PortV4SearchRequest from a dict
port_v4_search_request_from_dict = PortV4SearchRequest.from_dict(port_v4_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


