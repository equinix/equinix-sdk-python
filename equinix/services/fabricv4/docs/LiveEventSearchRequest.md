# LiveEventSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**LiveEventFilters**](LiveEventFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.live_event_search_request import LiveEventSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LiveEventSearchRequest from a JSON string
live_event_search_request_instance = LiveEventSearchRequest.from_json(json)
# print the JSON string representation of the object
print(LiveEventSearchRequest.to_json())

# convert the object into a dict
live_event_search_request_dict = live_event_search_request_instance.to_dict()
# create an instance of LiveEventSearchRequest from a dict
live_event_search_request_from_dict = LiveEventSearchRequest.from_dict(live_event_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


