# LoaNoteDetails

Represents a note added to a LOA by an  authorized user from either the issuer or requestor organization 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**LoaNoteDetailsType**](LoaNoteDetailsType.md) |  | [optional] 
**href** | **str** | URI to note resource. | [optional] 
**uuid** | **str** | Unique identifier of this note. | [optional] 
**comments** | **str** | Content of the note as submitted by the user. | [optional] 
**created_date_time** | **datetime** | Date and time when the note was created. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.loa_note_details import LoaNoteDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LoaNoteDetails from a JSON string
loa_note_details_instance = LoaNoteDetails.from_json(json)
# print the JSON string representation of the object
print(LoaNoteDetails.to_json())

# convert the object into a dict
loa_note_details_dict = loa_note_details_instance.to_dict()
# create an instance of LoaNoteDetails from a dict
loa_note_details_from_dict = LoaNoteDetails.from_dict(loa_note_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


