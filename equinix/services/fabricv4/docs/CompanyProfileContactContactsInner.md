# CompanyProfileContactContactsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**email** | **str** |  | 

## Example

```python
from equinix.services.fabricv4.models.company_profile_contact_contacts_inner import CompanyProfileContactContactsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyProfileContactContactsInner from a JSON string
company_profile_contact_contacts_inner_instance = CompanyProfileContactContactsInner.from_json(json)
# print the JSON string representation of the object
print(CompanyProfileContactContactsInner.to_json())

# convert the object into a dict
company_profile_contact_contacts_inner_dict = company_profile_contact_contacts_inner_instance.to_dict()
# create an instance of CompanyProfileContactContactsInner from a dict
company_profile_contact_contacts_inner_from_dict = CompanyProfileContactContactsInner.from_dict(company_profile_contact_contacts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


