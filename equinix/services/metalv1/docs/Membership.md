# Membership


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**project** | [**Href**](Href.md) |  | [optional] 
**roles** | **List[str]** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**user** | [**Href**](Href.md) |  | [optional] 

## Example

```python
from equinix_metal.models.membership import Membership

# TODO update the JSON string below
json = "{}"
# create an instance of Membership from a JSON string
membership_instance = Membership.from_json(json)
# print the JSON string representation of the object
print(Membership.to_json())

# convert the object into a dict
membership_dict = membership_instance.to_dict()
# create an instance of Membership from a dict
membership_form_dict = membership.from_dict(membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


