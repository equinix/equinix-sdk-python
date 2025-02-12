# Stream

Stream object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Stream URI | [optional] [readonly] 
**uuid** | **str** | Equinix-assigned access point identifier | [optional] 
**state** | **str** | Stream provision state | [optional] 
**assets_count** | **int** | Stream assets count | [optional] 
**stream_subscriptions_count** | **int** | Stream subscriptions count | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 
**type** | [**StreamPostRequestType**](StreamPostRequestType.md) |  | [optional] 
**name** | **str** | Customer-provided stream name | [optional] 
**description** | **str** | Customer-provided stream description | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream import Stream

# TODO update the JSON string below
json = "{}"
# create an instance of Stream from a JSON string
stream_instance = Stream.from_json(json)
# print the JSON string representation of the object
print(Stream.to_json())

# convert the object into a dict
stream_dict = stream_instance.to_dict()
# create an instance of Stream from a dict
stream_from_dict = Stream.from_dict(stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


