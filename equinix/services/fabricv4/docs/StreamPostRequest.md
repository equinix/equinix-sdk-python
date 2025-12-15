# StreamPostRequest

Create Stream

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**StreamPostRequestType**](StreamPostRequestType.md) |  | 
**name** | **str** | Customer-provided stream name | 
**description** | **str** | Customer-provided stream description | [optional] 
**project** | [**Project**](Project.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.stream_post_request import StreamPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StreamPostRequest from a JSON string
stream_post_request_instance = StreamPostRequest.from_json(json)
# print the JSON string representation of the object
print(StreamPostRequest.to_json())

# convert the object into a dict
stream_post_request_dict = stream_post_request_instance.to_dict()
# create an instance of StreamPostRequest from a dict
stream_post_request_from_dict = StreamPostRequest.from_dict(stream_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


