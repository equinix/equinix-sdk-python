# OrganizationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | [optional] 
**billing_address** | [**Address**](Address.md) |  | [optional] 
**customdata** | **object** |  | [optional] 
**description** | **str** |  | [optional] 
**enforce_2fa_at** | **datetime** | Force to all members to have enabled the two factor authentication after that date, unless the value is null | [optional] 
**href** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**twitter** | **str** |  | [optional] 
**website** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.organization_input import OrganizationInput

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationInput from a JSON string
organization_input_instance = OrganizationInput.from_json(json)
# print the JSON string representation of the object
print(OrganizationInput.to_json())

# convert the object into a dict
organization_input_dict = organization_input_instance.to_dict()
# create an instance of OrganizationInput from a dict
organization_input_form_dict = organization_input.from_dict(organization_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


