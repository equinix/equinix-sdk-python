# StreamPutRequest

Update Stream

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Customer-provided stream name | [optional] 
**description** | **str** | Customer-provided stream description | [optional] 
**enabled** | **bool** | stream state | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_put_request import StreamPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StreamPutRequest from a JSON string
stream_put_request_instance = StreamPutRequest.from_json(json)
# print the JSON string representation of the object
print(StreamPutRequest.to_json())

# convert the object into a dict
stream_put_request_dict = stream_put_request_instance.to_dict()
# create an instance of StreamPutRequest from a dict
stream_put_request_form_dict = stream_put_request.from_dict(stream_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


