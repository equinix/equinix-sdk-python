# MembershipInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**role** | **List[str]** |  | [optional] 

## Example

```python
from equinix_metal.models.membership_input import MembershipInput

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipInput from a JSON string
membership_input_instance = MembershipInput.from_json(json)
# print the JSON string representation of the object
print(MembershipInput.to_json())

# convert the object into a dict
membership_input_dict = membership_input_instance.to_dict()
# create an instance of MembershipInput from a dict
membership_input_form_dict = membership_input.from_dict(membership_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


