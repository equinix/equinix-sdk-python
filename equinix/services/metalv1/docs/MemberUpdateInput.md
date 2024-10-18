# MemberUpdateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bound_roles** | **List[str]** | Additional roles that can be bound to the user to grant extra permissions. | [optional] 
**href** | **str** |  | [optional] 
**project_ids** | **List[str]** | Project IDs the user should be able to access. This field is only required when role is set to &#x60;collaborator&#x60; or &#x60;limited_collaborator&#x60;. | [optional] 
**role** | **List[str]** | Primary role for the user within the organization | [optional] 

## Example

```python
from equinix.services.metalv1.models.member_update_input import MemberUpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of MemberUpdateInput from a JSON string
member_update_input_instance = MemberUpdateInput.from_json(json)
# print the JSON string representation of the object
print(MemberUpdateInput.to_json())

# convert the object into a dict
member_update_input_dict = member_update_input_instance.to_dict()
# create an instance of MemberUpdateInput from a dict
member_update_input_form_dict = member_update_input.from_dict(member_update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


