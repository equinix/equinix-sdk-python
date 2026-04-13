# ServiceProfileChange

Current state of latest service profile change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Uniquely identifies a change | [optional] 
**type** | **str** | Type of change | 
**status** | [**ServiceProfileChangeStatus**](ServiceProfileChangeStatus.md) |  | [optional] 
**created_date_time** | **datetime** | Set when change flow starts | 
**updated_date_time** | **datetime** | Set when change object is updated | [optional] 
**information** | **str** | Additional information | [optional] 
**data** | [**List[JsonPatchOperation]**](JsonPatchOperation.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_profile_change import ServiceProfileChange

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileChange from a JSON string
service_profile_change_instance = ServiceProfileChange.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileChange.to_json())

# convert the object into a dict
service_profile_change_dict = service_profile_change_instance.to_dict()
# create an instance of ServiceProfileChange from a dict
service_profile_change_from_dict = ServiceProfileChange.from_dict(service_profile_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


