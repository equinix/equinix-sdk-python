# InvitationList1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**invitations** | [**List[Membership]**](Membership.md) |  | [optional] 

## Example

```python
from equinix.services.metalv1.models.invitation_list1 import InvitationList1

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationList1 from a JSON string
invitation_list1_instance = InvitationList1.from_json(json)
# print the JSON string representation of the object
print(InvitationList1.to_json())

# convert the object into a dict
invitation_list1_dict = invitation_list1_instance.to_dict()
# create an instance of InvitationList1 from a dict
invitation_list1_from_dict = InvitationList1.from_dict(invitation_list1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


