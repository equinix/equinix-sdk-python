# Facility


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | [optional] 
**code** | **str** |  | [optional] 
**features** | **List[str]** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**ip_ranges** | **List[str]** | IP ranges registered in facility. Can be used for GeoIP location | [optional] 
**metro** | [**DeviceMetro**](DeviceMetro.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.facility import Facility

# TODO update the JSON string below
json = "{}"
# create an instance of Facility from a JSON string
facility_instance = Facility.from_json(json)
# print the JSON string representation of the object
print(Facility.to_json())

# convert the object into a dict
facility_dict = facility_instance.to_dict()
# create an instance of Facility from a dict
facility_form_dict = facility.from_dict(facility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


