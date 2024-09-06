# ServiceProfileAccessPointTypeVD

VirtualDevice Access Point Type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**type** | [**ServiceProfileAccessPointTypeEnum**](ServiceProfileAccessPointTypeEnum.md) |  | 
**supported_bandwidths** | **List[int]** |  | [optional] 
**allow_remote_connections** | **bool** | Allow remote connections to Service Profile | [optional] 
**allow_custom_bandwidth** | **bool** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_profile_access_point_type_vd import ServiceProfileAccessPointTypeVD

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileAccessPointTypeVD from a JSON string
service_profile_access_point_type_vd_instance = ServiceProfileAccessPointTypeVD.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileAccessPointTypeVD.to_json())

# convert the object into a dict
service_profile_access_point_type_vd_dict = service_profile_access_point_type_vd_instance.to_dict()
# create an instance of ServiceProfileAccessPointTypeVD from a dict
service_profile_access_point_type_vd_from_dict = ServiceProfileAccessPointTypeVD.from_dict(service_profile_access_point_type_vd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


