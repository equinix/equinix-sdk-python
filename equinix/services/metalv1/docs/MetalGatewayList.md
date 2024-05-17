# MetalGatewayList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 
**metal_gateways** | [**List[MetalGatewayListMetalGatewaysInner]**](MetalGatewayListMetalGatewaysInner.md) |  | [optional] 

## Example

```python
from equinix_metal.models.metal_gateway_list import MetalGatewayList

# TODO update the JSON string below
json = "{}"
# create an instance of MetalGatewayList from a JSON string
metal_gateway_list_instance = MetalGatewayList.from_json(json)
# print the JSON string representation of the object
print(MetalGatewayList.to_json())

# convert the object into a dict
metal_gateway_list_dict = metal_gateway_list_instance.to_dict()
# create an instance of MetalGatewayList from a dict
metal_gateway_list_form_dict = metal_gateway_list.from_dict(metal_gateway_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


