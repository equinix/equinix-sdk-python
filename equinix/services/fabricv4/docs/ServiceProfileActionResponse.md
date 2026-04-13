# ServiceProfileActionResponse

Service Profile Action Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Service Profile Action URI | [optional] [readonly] 
**type** | **str** | Action type. Example values: PROFILE_UPDATE_ACCEPTANCE, PROFILE_UPDATE_REJECTION | [optional] 
**uuid** | **str** | Equinix-assigned action identifier | [optional] 
**comments** | **str** | Action comments | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_profile_action_response import ServiceProfileActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileActionResponse from a JSON string
service_profile_action_response_instance = ServiceProfileActionResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileActionResponse.to_json())

# convert the object into a dict
service_profile_action_response_dict = service_profile_action_response_instance.to_dict()
# create an instance of ServiceProfileActionResponse from a dict
service_profile_action_response_from_dict = ServiceProfileActionResponse.from_dict(service_profile_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


