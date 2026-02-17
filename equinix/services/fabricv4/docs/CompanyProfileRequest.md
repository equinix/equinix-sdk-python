# CompanyProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | 
**summary** | **str** |  | 
**description** | **str** |  | 
**notifications** | **List[object]** |  | [optional] 
**web_url** | **str** |  | [optional] 
**contact_url** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.company_profile_request import CompanyProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyProfileRequest from a JSON string
company_profile_request_instance = CompanyProfileRequest.from_json(json)
# print the JSON string representation of the object
print(CompanyProfileRequest.to_json())

# convert the object into a dict
company_profile_request_dict = company_profile_request_instance.to_dict()
# create an instance of CompanyProfileRequest from a dict
company_profile_request_from_dict = CompanyProfileRequest.from_dict(company_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


