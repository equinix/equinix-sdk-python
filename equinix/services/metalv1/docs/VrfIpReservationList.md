# VrfIpReservationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**ip_addresses** | [**List[VrfIpReservation]**](VrfIpReservation.md) |  | [optional] 

## Example

```python
from equinix.services.metalv1.models.vrf_ip_reservation_list import VrfIpReservationList

# TODO update the JSON string below
json = "{}"
# create an instance of VrfIpReservationList from a JSON string
vrf_ip_reservation_list_instance = VrfIpReservationList.from_json(json)
# print the JSON string representation of the object
print(VrfIpReservationList.to_json())

# convert the object into a dict
vrf_ip_reservation_list_dict = vrf_ip_reservation_list_instance.to_dict()
# create an instance of VrfIpReservationList from a dict
vrf_ip_reservation_list_from_dict = VrfIpReservationList.from_dict(vrf_ip_reservation_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


