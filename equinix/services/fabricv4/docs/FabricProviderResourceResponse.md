# FabricProviderResourceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | IPWAN Connection URI | [optional] [readonly] 
**type** | **str** |  | 
**uuid** | **str** | Equinix-assigned ipwan connection identifier | [optional] 
**state** | [**DeploymentState**](DeploymentState.md) |  | 
**name** | **str** |  | 
**location** | [**SimplifiedLocation**](SimplifiedLocation.md) |  | 
**package** | [**CloudRouterPostRequestPackage**](CloudRouterPostRequestPackage.md) |  | 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | 
**bandwidth** | **int** |  | 
**redundancy** | [**ConnectionRedundancy**](ConnectionRedundancy.md) |  | 
**a_side** | [**ConnectionSide**](ConnectionSide.md) |  | 
**z_side** | [**ConnectionSide**](ConnectionSide.md) |  | 
**bgp_ipv4** | [**FabricBGPConnectionIpv4**](FabricBGPConnectionIpv4.md) |  | 
**customer_asn** | **int** | Customer asn | 
**bgp_auth_key** | **str** | BGP authorization key | 
**as_override_enabled** | **bool** | Enable AS number override | [optional] 
**scope** | [**NetworkScope**](NetworkScope.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.fabric_provider_resource_response import FabricProviderResourceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FabricProviderResourceResponse from a JSON string
fabric_provider_resource_response_instance = FabricProviderResourceResponse.from_json(json)
# print the JSON string representation of the object
print(FabricProviderResourceResponse.to_json())

# convert the object into a dict
fabric_provider_resource_response_dict = fabric_provider_resource_response_instance.to_dict()
# create an instance of FabricProviderResourceResponse from a dict
fabric_provider_resource_response_from_dict = FabricProviderResourceResponse.from_dict(fabric_provider_resource_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


