# ServiceProfileActionRequest

Service Profile Action Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Action type. Example values: PROFILE_UPDATE_ACCEPTANCE, PROFILE_UPDATE_REJECTION | 
**description** | **str** | Action description | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_profile_action_request import ServiceProfileActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileActionRequest from a JSON string
service_profile_action_request_instance = ServiceProfileActionRequest.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileActionRequest.to_json())

# convert the object into a dict
service_profile_action_request_dict = service_profile_action_request_instance.to_dict()
# create an instance of ServiceProfileActionRequest from a dict
service_profile_action_request_from_dict = ServiceProfileActionRequest.from_dict(service_profile_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


