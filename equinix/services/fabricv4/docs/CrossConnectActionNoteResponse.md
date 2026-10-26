# CrossConnectActionNoteResponse

Note the action applies to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Note URI. | [optional] [readonly] 
**uuid** | **str** | Note Identifier. | [optional] [readonly] 
**parent_note** | [**CrossConnectParentNote**](CrossConnectParentNote.md) | The note this note is responding to. Returned when the note was added in response to an Equinix note.  | [optional] [readonly] 
**comments** | **str** | Note comments. | [optional] [readonly] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_action_note_response import CrossConnectActionNoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectActionNoteResponse from a JSON string
cross_connect_action_note_response_instance = CrossConnectActionNoteResponse.from_json(json)
# print the JSON string representation of the object
print(CrossConnectActionNoteResponse.to_json())

# convert the object into a dict
cross_connect_action_note_response_dict = cross_connect_action_note_response_instance.to_dict()
# create an instance of CrossConnectActionNoteResponse from a dict
cross_connect_action_note_response_from_dict = CrossConnectActionNoteResponse.from_dict(cross_connect_action_note_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


