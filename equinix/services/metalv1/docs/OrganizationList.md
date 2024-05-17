# OrganizationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 
**organizations** | [**List[Organization]**](Organization.md) |  | [optional] 

## Example

```python
from equinix_metal.models.organization_list import OrganizationList

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationList from a JSON string
organization_list_instance = OrganizationList.from_json(json)
# print the JSON string representation of the object
print(OrganizationList.to_json())

# convert the object into a dict
organization_list_dict = organization_list_instance.to_dict()
# create an instance of OrganizationList from a dict
organization_list_form_dict = organization_list.from_dict(organization_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


