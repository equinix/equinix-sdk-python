# ServiceProfileAccessPointCOLO

Colo Access Point

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ServiceProfileAccessPointCOLOType**](ServiceProfileAccessPointCOLOType.md) |  | 
**uuid** | **str** |  | 
**location** | [**SimplifiedLocation**](SimplifiedLocation.md) |  | [optional] 
**seller_region** | **str** |  | [optional] 
**seller_region_description** | **str** |  | [optional] 
**cross_connect_id** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_profile_access_point_colo import ServiceProfileAccessPointCOLO

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileAccessPointCOLO from a JSON string
service_profile_access_point_colo_instance = ServiceProfileAccessPointCOLO.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileAccessPointCOLO.to_json())

# convert the object into a dict
service_profile_access_point_colo_dict = service_profile_access_point_colo_instance.to_dict()
# create an instance of ServiceProfileAccessPointCOLO from a dict
service_profile_access_point_colo_form_dict = service_profile_access_point_colo.from_dict(service_profile_access_point_colo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


