# ServiceProfileListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CompanyServiceProfile]**](CompanyServiceProfile.md) | List of service profiles | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_profile_list_response import ServiceProfileListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileListResponse from a JSON string
service_profile_list_response_instance = ServiceProfileListResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileListResponse.to_json())

# convert the object into a dict
service_profile_list_response_dict = service_profile_list_response_instance.to_dict()
# create an instance of ServiceProfileListResponse from a dict
service_profile_list_response_from_dict = ServiceProfileListResponse.from_dict(service_profile_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


