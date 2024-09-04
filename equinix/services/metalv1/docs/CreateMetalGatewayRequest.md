# CreateMetalGatewayRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**ip_reservation_id** | **str** | The UUID an a VRF IP Reservation that belongs to the same project as the one in which the Metal Gateway is to be created. Additionally, the VRF IP Reservation and the Virtual Network must reside in the same Metro. | 
**private_ipv4_subnet_size** | **int** | The subnet size (8, 16, 32, 64, or 128) of the private IPv4 reservation that will be created for the metal gateway. This field is required unless a project IP reservation was specified.           Please keep in mind that the number of private metal gateway ranges are limited per project. If you would like to increase the limit per project, please contact support for assistance. | [optional] 
**virtual_network_id** | **str** | The UUID of a Metro Virtual Network that belongs to the same project as the one in which the Metal Gateway is to be created. Additionally, the Virtual Network and the VRF IP Reservation must reside in the same metro. In the case of the IP reservation being an IPv6 based VRF IP Reservation, the Virtual Network must not already have an associated IPv6 based VRF IP Reservation. There can be exactly one IPv6 based VRF IP Reservation associated to a Virtual Network. | 

## Example

```python
from equinix_metal.models.create_metal_gateway_request import CreateMetalGatewayRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMetalGatewayRequest from a JSON string
create_metal_gateway_request_instance = CreateMetalGatewayRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMetalGatewayRequest.to_json())

# convert the object into a dict
create_metal_gateway_request_dict = create_metal_gateway_request_instance.to_dict()
# create an instance of CreateMetalGatewayRequest from a dict
create_metal_gateway_request_form_dict = create_metal_gateway_request.from_dict(create_metal_gateway_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


