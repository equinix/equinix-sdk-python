# ServiceProfileAccessPointVD

Virtual Device Point

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ServiceProfileAccessPointVDType**](ServiceProfileAccessPointVDType.md) |  | 
**uuid** | **str** |  | 
**location** | [**SimplifiedLocation**](SimplifiedLocation.md) |  | [optional] 
**interface_uuid** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_profile_access_point_vd import ServiceProfileAccessPointVD

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileAccessPointVD from a JSON string
service_profile_access_point_vd_instance = ServiceProfileAccessPointVD.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileAccessPointVD.to_json())

# convert the object into a dict
service_profile_access_point_vd_dict = service_profile_access_point_vd_instance.to_dict()
# create an instance of ServiceProfileAccessPointVD from a dict
service_profile_access_point_vd_from_dict = ServiceProfileAccessPointVD.from_dict(service_profile_access_point_vd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


