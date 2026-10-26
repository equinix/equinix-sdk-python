# SearchLiveEventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[CloudEvent]**](CloudEvent.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.search_live_event_response import SearchLiveEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchLiveEventResponse from a JSON string
search_live_event_response_instance = SearchLiveEventResponse.from_json(json)
# print the JSON string representation of the object
print(SearchLiveEventResponse.to_json())

# convert the object into a dict
search_live_event_response_dict = search_live_event_response_instance.to_dict()
# create an instance of SearchLiveEventResponse from a dict
search_live_event_response_from_dict = SearchLiveEventResponse.from_dict(search_live_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


