# ServiceProfiles

Service Profiles

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ServiceProfile]**](ServiceProfile.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_profiles import ServiceProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfiles from a JSON string
service_profiles_instance = ServiceProfiles.from_json(json)
# print the JSON string representation of the object
print(ServiceProfiles.to_json())

# convert the object into a dict
service_profiles_dict = service_profiles_instance.to_dict()
# create an instance of ServiceProfiles from a dict
service_profiles_from_dict = ServiceProfiles.from_dict(service_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


