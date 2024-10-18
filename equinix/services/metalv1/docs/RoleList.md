# RoleList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**roles** | [**List[RoleListRolesInner]**](RoleListRolesInner.md) |  | [optional] 

## Example

```python
from equinix.services.metalv1.models.role_list import RoleList

# TODO update the JSON string below
json = "{}"
# create an instance of RoleList from a JSON string
role_list_instance = RoleList.from_json(json)
# print the JSON string representation of the object
print(RoleList.to_json())

# convert the object into a dict
role_list_dict = role_list_instance.to_dict()
# create an instance of RoleList from a dict
role_list_form_dict = role_list.from_dict(role_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


