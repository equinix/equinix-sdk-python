# CrossConnectNotesResponse

List of notes added to the Cross Connect.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[CrossConnectNoteResponse]**](CrossConnectNoteResponse.md) |  | [optional] [readonly] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_notes_response import CrossConnectNotesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectNotesResponse from a JSON string
cross_connect_notes_response_instance = CrossConnectNotesResponse.from_json(json)
# print the JSON string representation of the object
print(CrossConnectNotesResponse.to_json())

# convert the object into a dict
cross_connect_notes_response_dict = cross_connect_notes_response_instance.to_dict()
# create an instance of CrossConnectNotesResponse from a dict
cross_connect_notes_response_from_dict = CrossConnectNotesResponse.from_dict(cross_connect_notes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


