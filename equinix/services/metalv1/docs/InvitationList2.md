# InvitationList2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**invitations** | [**List[Membership]**](Membership.md) |  | [optional] 

## Example

```python
from equinix.services.metalv1.models.invitation_list2 import InvitationList2

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationList2 from a JSON string
invitation_list2_instance = InvitationList2.from_json(json)
# print the JSON string representation of the object
print(InvitationList2.to_json())

# convert the object into a dict
invitation_list2_dict = invitation_list2_instance.to_dict()
# create an instance of InvitationList2 from a dict
invitation_list2_from_dict = InvitationList2.from_dict(invitation_list2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


