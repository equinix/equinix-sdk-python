# MembershipList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**memberships** | [**List[Membership]**](Membership.md) |  | [optional] 

## Example

```python
from equinix_metal.models.membership_list import MembershipList

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipList from a JSON string
membership_list_instance = MembershipList.from_json(json)
# print the JSON string representation of the object
print(MembershipList.to_json())

# convert the object into a dict
membership_list_dict = membership_list_instance.to_dict()
# create an instance of MembershipList from a dict
membership_list_form_dict = membership_list.from_dict(membership_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


