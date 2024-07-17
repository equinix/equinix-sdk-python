# FabricCloudRouterPrice

Cloud Router  Product configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique identifier assigned to the Cloud Router | [optional] 
**location** | [**PriceLocation**](PriceLocation.md) |  | [optional] 
**package** | [**FabricCloudRouterPackages**](FabricCloudRouterPackages.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.fabric_cloud_router_price import FabricCloudRouterPrice

# TODO update the JSON string below
json = "{}"
# create an instance of FabricCloudRouterPrice from a JSON string
fabric_cloud_router_price_instance = FabricCloudRouterPrice.from_json(json)
# print the JSON string representation of the object
print(FabricCloudRouterPrice.to_json())

# convert the object into a dict
fabric_cloud_router_price_dict = fabric_cloud_router_price_instance.to_dict()
# create an instance of FabricCloudRouterPrice from a dict
fabric_cloud_router_price_form_dict = fabric_cloud_router_price.from_dict(fabric_cloud_router_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


