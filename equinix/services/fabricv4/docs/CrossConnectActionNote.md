# CrossConnectActionNote

Note supplied by the customer when responding to an action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_note** | [**CrossConnectParentNote**](CrossConnectParentNote.md) |  | [optional] 
**comments** | **str** | Note comments. | 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_action_note import CrossConnectActionNote

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectActionNote from a JSON string
cross_connect_action_note_instance = CrossConnectActionNote.from_json(json)
# print the JSON string representation of the object
print(CrossConnectActionNote.to_json())

# convert the object into a dict
cross_connect_action_note_dict = cross_connect_action_note_instance.to_dict()
# create an instance of CrossConnectActionNote from a dict
cross_connect_action_note_from_dict = CrossConnectActionNote.from_dict(cross_connect_action_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


