# MetalGatewayListMetalGatewaysInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**created_by** | [**Href**](Href.md) |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**ip_reservation** | [**VrfIpReservation**](VrfIpReservation.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**state** | **str** | The current state of the Metal Gateway. &#39;Ready&#39; indicates the gateway record has been configured, but is currently not active on the network. &#39;Active&#39; indicates the gateway has been configured on the network. &#39;Deleting&#39; is a temporary state used to indicate that the gateway is in the process of being un-configured from the network, after which the gateway record will be deleted. | [optional] 
**updated_at** | **datetime** |  | [optional] 
**virtual_network** | [**VirtualNetwork**](VirtualNetwork.md) |  | [optional] 
**vrf** | [**Vrf**](Vrf.md) |  | [optional] 

## Example

```python
from equinix_metal.models.metal_gateway_list_metal_gateways_inner import MetalGatewayListMetalGatewaysInner

# TODO update the JSON string below
json = "{}"
# create an instance of MetalGatewayListMetalGatewaysInner from a JSON string
metal_gateway_list_metal_gateways_inner_instance = MetalGatewayListMetalGatewaysInner.from_json(json)
# print the JSON string representation of the object
print(MetalGatewayListMetalGatewaysInner.to_json())

# convert the object into a dict
metal_gateway_list_metal_gateways_inner_dict = metal_gateway_list_metal_gateways_inner_instance.to_dict()
# create an instance of MetalGatewayListMetalGatewaysInner from a dict
metal_gateway_list_metal_gateways_inner_form_dict = metal_gateway_list_metal_gateways_inner.from_dict(metal_gateway_list_metal_gateways_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


