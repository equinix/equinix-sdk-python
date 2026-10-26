# CrossConnectNoteResponse

Cross Connect Note.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Note URI. | [optional] [readonly] 
**uuid** | **str** | Note Identifier. | [optional] [readonly] 
**type** | [**CrossConnectNoteResponseType**](CrossConnectNoteResponseType.md) |  | [optional] 
**source** | [**CrossConnectNoteResponseSource**](CrossConnectNoteResponseSource.md) |  | [optional] 
**comments** | **str** | Note comments. | [optional] [readonly] 
**parent_note** | [**CrossConnectParentNote**](CrossConnectParentNote.md) | The note this note is responding to. Returned when the note was added in response to an Equinix note.  | [optional] [readonly] 
**change_log** | [**CrossConnectChangelog**](CrossConnectChangelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_note_response import CrossConnectNoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectNoteResponse from a JSON string
cross_connect_note_response_instance = CrossConnectNoteResponse.from_json(json)
# print the JSON string representation of the object
print(CrossConnectNoteResponse.to_json())

# convert the object into a dict
cross_connect_note_response_dict = cross_connect_note_response_instance.to_dict()
# create an instance of CrossConnectNoteResponse from a dict
cross_connect_note_response_from_dict = CrossConnectNoteResponse.from_dict(cross_connect_note_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


