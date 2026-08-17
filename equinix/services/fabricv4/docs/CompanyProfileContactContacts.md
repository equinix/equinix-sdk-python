# CompanyProfileContactContacts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**email** | **str** |  | 

## Example

```python
from equinix.services.fabricv4.models.company_profile_contact_contacts import CompanyProfileContactContacts

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyProfileContactContacts from a JSON string
company_profile_contact_contacts_instance = CompanyProfileContactContacts.from_json(json)
# print the JSON string representation of the object
print(CompanyProfileContactContacts.to_json())

# convert the object into a dict
company_profile_contact_contacts_dict = company_profile_contact_contacts_instance.to_dict()
# create an instance of CompanyProfileContactContacts from a dict
company_profile_contact_contacts_from_dict = CompanyProfileContactContacts.from_dict(company_profile_contact_contacts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


