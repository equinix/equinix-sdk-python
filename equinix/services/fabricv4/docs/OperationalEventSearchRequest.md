# OperationalEventSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**OperationalEventFilters**](OperationalEventFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.operational_event_search_request import OperationalEventSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OperationalEventSearchRequest from a JSON string
operational_event_search_request_instance = OperationalEventSearchRequest.from_json(json)
# print the JSON string representation of the object
print(OperationalEventSearchRequest.to_json())

# convert the object into a dict
operational_event_search_request_dict = operational_event_search_request_instance.to_dict()
# create an instance of OperationalEventSearchRequest from a dict
operational_event_search_request_from_dict = OperationalEventSearchRequest.from_dict(operational_event_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


