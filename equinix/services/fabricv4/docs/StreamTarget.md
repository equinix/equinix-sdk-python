# StreamTarget

Stream uuid

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Stream UUID | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_target import StreamTarget

# TODO update the JSON string below
json = "{}"
# create an instance of StreamTarget from a JSON string
stream_target_instance = StreamTarget.from_json(json)
# print the JSON string representation of the object
print(StreamTarget.to_json())

# convert the object into a dict
stream_target_dict = stream_target_instance.to_dict()
# create an instance of StreamTarget from a dict
stream_target_from_dict = StreamTarget.from_dict(stream_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


