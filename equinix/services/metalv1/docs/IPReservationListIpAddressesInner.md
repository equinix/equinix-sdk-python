# IPReservationListIpAddressesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon** | **bool** |  | [optional] 
**address** | **str** |  | [optional] 
**address_family** | **int** |  | [optional] 
**assignments** | [**List[Href]**](Href.md) |  | [optional] 
**available** | **str** |  | [optional] 
**bill** | **bool** |  | [optional] 
**cidr** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**customdata** | **object** |  | [optional] 
**details** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**facility** | [**IPReservationFacility**](IPReservationFacility.md) |  | [optional] 
**gateway** | **str** |  | [optional] 
**global_ip** | **bool** |  | [optional] 
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
**requested_by** | [**Href**](Href.md) |  | [optional] 
**state** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**type** | **str** |  | 
**created_by** | [**Href**](Href.md) |  | [optional] 
**vrf** | [**Vrf**](Vrf.md) |  | 

## Example

```python
from equinix_metal.models.ip_reservation_list_ip_addresses_inner import IPReservationListIpAddressesInner

# TODO update the JSON string below
json = "{}"
# create an instance of IPReservationListIpAddressesInner from a JSON string
ip_reservation_list_ip_addresses_inner_instance = IPReservationListIpAddressesInner.from_json(json)
# print the JSON string representation of the object
print(IPReservationListIpAddressesInner.to_json())

# convert the object into a dict
ip_reservation_list_ip_addresses_inner_dict = ip_reservation_list_ip_addresses_inner_instance.to_dict()
# create an instance of IPReservationListIpAddressesInner from a dict
ip_reservation_list_ip_addresses_inner_form_dict = ip_reservation_list_ip_addresses_inner.from_dict(ip_reservation_list_ip_addresses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


