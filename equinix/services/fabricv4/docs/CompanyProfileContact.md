# CompanyProfileContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CompanyProfileContactType**](CompanyProfileContactType.md) |  | [optional] 
**contacts** | [**List[CompanyProfileContactContacts]**](CompanyProfileContactContacts.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.company_profile_contact import CompanyProfileContact

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyProfileContact from a JSON string
company_profile_contact_instance = CompanyProfileContact.from_json(json)
# print the JSON string representation of the object
print(CompanyProfileContact.to_json())

# convert the object into a dict
company_profile_contact_dict = company_profile_contact_instance.to_dict()
# create an instance of CompanyProfileContact from a dict
company_profile_contact_from_dict = CompanyProfileContact.from_dict(company_profile_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


