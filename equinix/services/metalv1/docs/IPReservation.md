# IPReservation


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
**metro** | [**IPReservationMetro**](IPReservationMetro.md) |  | [optional] 
**netmask** | **str** |  | [optional] 
**network** | **str** |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**project_lite** | [**Href**](Href.md) |  | [optional] 
**public** | **bool** |  | [optional] 
**requested_by** | [**Href**](Href.md) |  | [optional] 
**state** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from equinix_metal.models.ip_reservation import IPReservation

# TODO update the JSON string below
json = "{}"
# create an instance of IPReservation from a JSON string
ip_reservation_instance = IPReservation.from_json(json)
# print the JSON string representation of the object
print(IPReservation.to_json())

# convert the object into a dict
ip_reservation_dict = ip_reservation_instance.to_dict()
# create an instance of IPReservation from a dict
ip_reservation_form_dict = ip_reservation.from_dict(ip_reservation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


