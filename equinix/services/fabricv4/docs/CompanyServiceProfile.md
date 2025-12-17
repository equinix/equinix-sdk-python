# CompanyServiceProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.company_service_profile import CompanyServiceProfile

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyServiceProfile from a JSON string
company_service_profile_instance = CompanyServiceProfile.from_json(json)
# print the JSON string representation of the object
print(CompanyServiceProfile.to_json())

# convert the object into a dict
company_service_profile_dict = company_service_profile_instance.to_dict()
# create an instance of CompanyServiceProfile from a dict
company_service_profile_from_dict = CompanyServiceProfile.from_dict(company_service_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


