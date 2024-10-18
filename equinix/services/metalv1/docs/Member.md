# Member


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bound_roles** | **List[str]** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**organization** | [**Href**](Href.md) |  | [optional] 
**projects** | [**List[Href]**](Href.md) |  | [optional] 
**projects_count** | **int** |  | [optional] 
**roles** | **List[str]** |  | [optional] 
**user** | [**Href**](Href.md) |  | [optional] 

## Example

```python
from equinix.services.metalv1.models.member import Member

# TODO update the JSON string below
json = "{}"
# create an instance of Member from a JSON string
member_instance = Member.from_json(json)
# print the JSON string representation of the object
print(Member.to_json())

# convert the object into a dict
member_dict = member_instance.to_dict()
# create an instance of Member from a dict
member_form_dict = member.from_dict(member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


