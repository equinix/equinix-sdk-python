# VrfIpReservationCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidr** | **int** | The size of the VRF IP Reservation&#39;s subnet. The following subnet sizes are supported: - IPv4: between 22 - 29 inclusive - IPv6: exactly 64  | 
**customdata** | **object** |  | [optional] 
**details** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**network** | **str** | The starting address for this VRF IP Reservation&#39;s subnet. Both IPv4 and IPv6 are supported. | 
**tags** | **List[str]** |  | [optional] 
**type** | **str** | Must be set to &#39;vrf&#39; | 
**vrf_id** | **str** | The ID of the VRF in which this VRF IP Reservation is created. The VRF must have an existing IP Range that contains the requested subnet. This field may be aliased as just &#39;vrf&#39;. | 

## Example

```python
from equinix_metal.models.vrf_ip_reservation_create_input import VrfIpReservationCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of VrfIpReservationCreateInput from a JSON string
vrf_ip_reservation_create_input_instance = VrfIpReservationCreateInput.from_json(json)
# print the JSON string representation of the object
print(VrfIpReservationCreateInput.to_json())

# convert the object into a dict
vrf_ip_reservation_create_input_dict = vrf_ip_reservation_create_input_instance.to_dict()
# create an instance of VrfIpReservationCreateInput from a dict
vrf_ip_reservation_create_input_form_dict = vrf_ip_reservation_create_input.from_dict(vrf_ip_reservation_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


