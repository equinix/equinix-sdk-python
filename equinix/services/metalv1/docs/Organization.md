# Organization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | [optional] 
**billing_address** | [**Address**](Address.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**credit_amount** | **float** |  | [optional] 
**customdata** | **object** |  | [optional] 
**description** | **str** |  | [optional] 
**enforce_2fa_at** | **datetime** | Force to all members to have enabled the two factor authentication after that date, unless the value is null | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**members** | [**List[Href]**](Href.md) |  | [optional] 
**memberships** | [**List[Href]**](Href.md) |  | [optional] 
**name** | **str** |  | [optional] 
**projects** | [**List[Href]**](Href.md) |  | [optional] 
**terms** | **int** |  | [optional] 
**twitter** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**website** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.organization import Organization

# TODO update the JSON string below
json = "{}"
# create an instance of Organization from a JSON string
organization_instance = Organization.from_json(json)
# print the JSON string representation of the object
print(Organization.to_json())

# convert the object into a dict
organization_dict = organization_instance.to_dict()
# create an instance of Organization from a dict
organization_form_dict = organization.from_dict(organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


