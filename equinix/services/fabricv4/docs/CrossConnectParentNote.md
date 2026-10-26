# CrossConnectParentNote

Note that this note is responding to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Parent note URI. | [optional] [readonly] 
**uuid** | **str** | Parent note UUID. | 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_parent_note import CrossConnectParentNote

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectParentNote from a JSON string
cross_connect_parent_note_instance = CrossConnectParentNote.from_json(json)
# print the JSON string representation of the object
print(CrossConnectParentNote.to_json())

# convert the object into a dict
cross_connect_parent_note_dict = cross_connect_parent_note_instance.to_dict()
# create an instance of CrossConnectParentNote from a dict
cross_connect_parent_note_from_dict = CrossConnectParentNote.from_dict(cross_connect_parent_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


