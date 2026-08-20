# LoaNotesResponse

List of Loa note details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[LoaNoteDetails]**](LoaNoteDetails.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.loa_notes_response import LoaNotesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LoaNotesResponse from a JSON string
loa_notes_response_instance = LoaNotesResponse.from_json(json)
# print the JSON string representation of the object
print(LoaNotesResponse.to_json())

# convert the object into a dict
loa_notes_response_dict = loa_notes_response_instance.to_dict()
# create an instance of LoaNotesResponse from a dict
loa_notes_response_from_dict = LoaNotesResponse.from_dict(loa_notes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


