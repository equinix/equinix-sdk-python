# IPReservationListIpAddressesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_family** | **int** |  | [optional] 
**cidr** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by** | [**Href**](Href.md) |  | [optional] 
**details** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**metal_gateway** | [**MetalGatewayLite**](MetalGatewayLite.md) |  | [optional] 
**netmask** | **str** |  | [optional] 
**network** | **str** |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**state** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**type** | **str** |  | 
**vrf** | [**Vrf**](Vrf.md) |  | 
**public** | **bool** |  | [optional] 
**management** | **bool** |  | [optional] 
**manageable** | **bool** |  | [optional] 
**customdata** | **object** |  | [optional] 
**bill** | **bool** |  | [optional] 
**project_lite** | [**Project**](Project.md) |  | [optional] 
**address** | **str** |  | [optional] 
**gateway** | **str** |  | [optional] 
**metro** | [**Metro**](Metro.md) |  | [optional] 

## Example

```python
from equinix.services.metalv1.models.ip_reservation_list_ip_addresses_inner import IPReservationListIpAddressesInner

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


