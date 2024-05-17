# MetalGatewayCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**ip_reservation_id** | **str** | The UUID of an IP reservation that belongs to the same project as where the metal gateway will be created in. This field is required unless the private IPv4 subnet size is specified. | [optional] 
**private_ipv4_subnet_size** | **int** | The subnet size (8, 16, 32, 64, or 128) of the private IPv4 reservation that will be created for the metal gateway. This field is required unless a project IP reservation was specified.           Please keep in mind that the number of private metal gateway ranges are limited per project. If you would like to increase the limit per project, please contact support for assistance. | [optional] 
**virtual_network_id** | **str** | The UUID of a metro virtual network that belongs to the same project as where the metal gateway will be created in. | 

## Example

```python
from equinix_metal.models.metal_gateway_create_input import MetalGatewayCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of MetalGatewayCreateInput from a JSON string
metal_gateway_create_input_instance = MetalGatewayCreateInput.from_json(json)
# print the JSON string representation of the object
print(MetalGatewayCreateInput.to_json())

# convert the object into a dict
metal_gateway_create_input_dict = metal_gateway_create_input_instance.to_dict()
# create an instance of MetalGatewayCreateInput from a dict
metal_gateway_create_input_form_dict = metal_gateway_create_input.from_dict(metal_gateway_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


