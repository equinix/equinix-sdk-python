# CrossConnectNoteRequest

Cross Connect Note.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** | Note comments. | 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_note_request import CrossConnectNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectNoteRequest from a JSON string
cross_connect_note_request_instance = CrossConnectNoteRequest.from_json(json)
# print the JSON string representation of the object
print(CrossConnectNoteRequest.to_json())

# convert the object into a dict
cross_connect_note_request_dict = cross_connect_note_request_instance.to_dict()
# create an instance of CrossConnectNoteRequest from a dict
cross_connect_note_request_from_dict = CrossConnectNoteRequest.from_dict(cross_connect_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


