# IPReservationFacility


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
from equinix_metal.models.ip_reservation_facility import IPReservationFacility

# TODO update the JSON string below
json = "{}"
# create an instance of IPReservationFacility from a JSON string
ip_reservation_facility_instance = IPReservationFacility.from_json(json)
# print the JSON string representation of the object
print(IPReservationFacility.to_json())

# convert the object into a dict
ip_reservation_facility_dict = ip_reservation_facility_instance.to_dict()
# create an instance of IPReservationFacility from a dict
ip_reservation_facility_form_dict = ip_reservation_facility.from_dict(ip_reservation_facility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


