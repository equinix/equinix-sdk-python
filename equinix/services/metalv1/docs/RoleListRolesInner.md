# RoleListRolesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from equinix.services.metalv1.models.role_list_roles_inner import RoleListRolesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RoleListRolesInner from a JSON string
role_list_roles_inner_instance = RoleListRolesInner.from_json(json)
# print the JSON string representation of the object
print(RoleListRolesInner.to_json())

# convert the object into a dict
role_list_roles_inner_dict = role_list_roles_inner_instance.to_dict()
# create an instance of RoleListRolesInner from a dict
role_list_roles_inner_form_dict = role_list_roles_inner.from_dict(role_list_roles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


