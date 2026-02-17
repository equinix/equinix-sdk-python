# CompanyProfileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**state** | **object** |  | [optional] 
**metros** | [**List[CompanyMetro]**](CompanyMetro.md) |  | [optional] 
**logo** | [**CompanyLogo**](CompanyLogo.md) |  | [optional] 
**tags** | [**List[TagResponse]**](TagResponse.md) |  | [optional] 
**service_profiles** | [**List[CompanyServiceProfile]**](CompanyServiceProfile.md) |  | [optional] 
**private_services** | [**List[PrivateService]**](PrivateService.md) |  | [optional] 
**notifications** | **List[object]** |  | [optional] 
**web_url** | **str** |  | [optional] 
**contact_url** | **str** |  | [optional] 
**change** | [**CompanyProfileChange**](CompanyProfileChange.md) |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.company_profile_response import CompanyProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyProfileResponse from a JSON string
company_profile_response_instance = CompanyProfileResponse.from_json(json)
# print the JSON string representation of the object
print(CompanyProfileResponse.to_json())

# convert the object into a dict
company_profile_response_dict = company_profile_response_instance.to_dict()
# create an instance of CompanyProfileResponse from a dict
company_profile_response_from_dict = CompanyProfileResponse.from_dict(company_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


