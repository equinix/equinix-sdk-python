# CreateLoaNote

Create Loa Note

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** | The note content to add to this LOA. Notes are visible to both the issuer and requestor organizations. Use notes to communicate updates, clarifications, or additional context about the LOA.  | 

## Example

```python
from equinix.services.fabricv4.models.create_loa_note import CreateLoaNote

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLoaNote from a JSON string
create_loa_note_instance = CreateLoaNote.from_json(json)
# print the JSON string representation of the object
print(CreateLoaNote.to_json())

# convert the object into a dict
create_loa_note_dict = create_loa_note_instance.to_dict()
# create an instance of CreateLoaNote from a dict
create_loa_note_from_dict = CreateLoaNote.from_dict(create_loa_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


