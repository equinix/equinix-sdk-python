# VrfMetalGatewayCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**ip_reservation_id** | **str** | The UUID an a VRF IP Reservation that belongs to the same project as the one in which the Metal Gateway is to be created. Additionally, the VRF IP Reservation and the Virtual Network must reside in the same Metro. | 
**virtual_network_id** | **str** | THe UUID of a Metro Virtual Network that belongs to the same project as the one in which the Metal Gateway is to be created. Additionally, the Virtual Network and the VRF IP Reservation must reside in the same metro. | 

## Example

```python
from equinix_metal.models.vrf_metal_gateway_create_input import VrfMetalGatewayCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of VrfMetalGatewayCreateInput from a JSON string
vrf_metal_gateway_create_input_instance = VrfMetalGatewayCreateInput.from_json(json)
# print the JSON string representation of the object
print(VrfMetalGatewayCreateInput.to_json())

# convert the object into a dict
vrf_metal_gateway_create_input_dict = vrf_metal_gateway_create_input_instance.to_dict()
# create an instance of VrfMetalGatewayCreateInput from a dict
vrf_metal_gateway_create_input_form_dict = vrf_metal_gateway_create_input.from_dict(vrf_metal_gateway_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


