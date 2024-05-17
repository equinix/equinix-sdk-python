# VrfIpReservation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**address_family** | **int** |  | [optional] 
**bill** | **bool** |  | [optional] 
**cidr** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by** | [**Href**](Href.md) |  | [optional] 
**customdata** | **object** |  | [optional] 
**details** | **str** |  | [optional] 
**gateway** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**manageable** | **bool** |  | [optional] 
**management** | **bool** |  | [optional] 
**metal_gateway** | [**MetalGatewayLite**](MetalGatewayLite.md) |  | [optional] 
**metro** | [**Metro**](Metro.md) |  | [optional] 
**netmask** | **str** |  | [optional] 
**network** | **str** |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**project_lite** | [**Project**](Project.md) |  | [optional] 
**public** | **bool** |  | [optional] 
**state** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**type** | **str** |  | 
**vrf** | [**Vrf**](Vrf.md) |  | 

## Example

```python
from equinix_metal.models.vrf_ip_reservation import VrfIpReservation

# TODO update the JSON string below
json = "{}"
# create an instance of VrfIpReservation from a JSON string
vrf_ip_reservation_instance = VrfIpReservation.from_json(json)
# print the JSON string representation of the object
print(VrfIpReservation.to_json())

# convert the object into a dict
vrf_ip_reservation_dict = vrf_ip_reservation_instance.to_dict()
# create an instance of VrfIpReservation from a dict
vrf_ip_reservation_form_dict = vrf_ip_reservation.from_dict(vrf_ip_reservation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


