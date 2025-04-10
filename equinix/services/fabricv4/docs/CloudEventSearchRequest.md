# CloudEventSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**CloudEventFilters**](CloudEventFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[CloudEventFilters]**](CloudEventFilters.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_event_search_request import CloudEventSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloudEventSearchRequest from a JSON string
cloud_event_search_request_instance = CloudEventSearchRequest.from_json(json)
# print the JSON string representation of the object
print(CloudEventSearchRequest.to_json())

# convert the object into a dict
cloud_event_search_request_dict = cloud_event_search_request_instance.to_dict()
# create an instance of CloudEventSearchRequest from a dict
cloud_event_search_request_from_dict = CloudEventSearchRequest.from_dict(cloud_event_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


