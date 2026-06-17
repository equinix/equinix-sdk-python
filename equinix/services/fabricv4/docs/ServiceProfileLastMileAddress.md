# ServiceProfileLastMileAddress

Last-mile provisioning address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**require** | **bool** | Whether the address is required for provisioning and ordering. | [optional] 
**data_type** | **str** | Expected format of the address. | [optional] 
**description** | **str** | Additional information about the address requirement. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_profile_last_mile_address import ServiceProfileLastMileAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileLastMileAddress from a JSON string
service_profile_last_mile_address_instance = ServiceProfileLastMileAddress.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileLastMileAddress.to_json())

# convert the object into a dict
service_profile_last_mile_address_dict = service_profile_last_mile_address_instance.to_dict()
# create an instance of ServiceProfileLastMileAddress from a dict
service_profile_last_mile_address_from_dict = ServiceProfileLastMileAddress.from_dict(service_profile_last_mile_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


