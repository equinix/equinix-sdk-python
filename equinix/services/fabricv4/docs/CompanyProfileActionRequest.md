# CompanyProfileActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | CompanyProfile Action Type | 
**comments** | **str** | Optional comments for the action | [optional] 

## Example

```python
from equinix.services.fabricv4.models.company_profile_action_request import CompanyProfileActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyProfileActionRequest from a JSON string
company_profile_action_request_instance = CompanyProfileActionRequest.from_json(json)
# print the JSON string representation of the object
print(CompanyProfileActionRequest.to_json())

# convert the object into a dict
company_profile_action_request_dict = company_profile_action_request_instance.to_dict()
# create an instance of CompanyProfileActionRequest from a dict
company_profile_action_request_from_dict = CompanyProfileActionRequest.from_dict(company_profile_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


