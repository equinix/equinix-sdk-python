# ConnectionCompanyProfile

Connection Company Profile Details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | company profile identifier | [optional] 
**name** | **str** | company profile name | [optional] 
**global_org_id** | **str** | global customer organization value | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connection_company_profile import ConnectionCompanyProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionCompanyProfile from a JSON string
connection_company_profile_instance = ConnectionCompanyProfile.from_json(json)
# print the JSON string representation of the object
print(ConnectionCompanyProfile.to_json())

# convert the object into a dict
connection_company_profile_dict = connection_company_profile_instance.to_dict()
# create an instance of ConnectionCompanyProfile from a dict
connection_company_profile_form_dict = connection_company_profile.from_dict(connection_company_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


