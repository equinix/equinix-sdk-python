# FabricProviderResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | 
**uuid** | **str** | Equinix-assigned access point identifier | [optional] 
**location** | [**SimplifiedLocation**](SimplifiedLocation.md) |  | [optional] 
**package** | [**CloudRouterPostRequestPackage**](CloudRouterPostRequestPackage.md) |  | [optional] 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | 
**bandwidth** | **int** |  | 
**redundancy** | [**ConnectionRedundancy**](ConnectionRedundancy.md) |  | 
**a_side** | [**ConnectionSide**](ConnectionSide.md) |  | 
**z_side** | [**ConnectionSide**](ConnectionSide.md) |  | 
**bgp_ipv4** | [**FabricBGPConnectionIpv4**](FabricBGPConnectionIpv4.md) |  | 
**customer_asn** | **int** | Customer asn | 
**bgp_auth_key** | **str** | BGP authorization key | 
**as_override_enabled** | **bool** | Enable AS number override | [optional] 
**scope** | [**NetworkScope**](NetworkScope.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.fabric_provider_resource import FabricProviderResource

# TODO update the JSON string below
json = "{}"
# create an instance of FabricProviderResource from a JSON string
fabric_provider_resource_instance = FabricProviderResource.from_json(json)
# print the JSON string representation of the object
print(FabricProviderResource.to_json())

# convert the object into a dict
fabric_provider_resource_dict = fabric_provider_resource_instance.to_dict()
# create an instance of FabricProviderResource from a dict
fabric_provider_resource_from_dict = FabricProviderResource.from_dict(fabric_provider_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


