# InvitationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**invitee** | **str** |  | 
**message** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**projects_ids** | **List[str]** |  | [optional] 
**roles** | **List[str]** |  | [optional] 

## Example

```python
from equinix_metal.models.invitation_input import InvitationInput

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationInput from a JSON string
invitation_input_instance = InvitationInput.from_json(json)
# print the JSON string representation of the object
print(InvitationInput.to_json())

# convert the object into a dict
invitation_input_dict = invitation_input_instance.to_dict()
# create an instance of InvitationInput from a dict
invitation_input_form_dict = invitation_input.from_dict(invitation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


