# GCPCloudRouter

The GCP CloudRouter schema defines the structure for the gcp cloud router configuration, including provider type, VPC, subnet, and deployment properties. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**GCPCloudRouterType**](GCPCloudRouterType.md) |  | 
**vpc_id** | **str** |  | 
**subnet_id** | **str** |  | 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.gcp_cloud_router import GCPCloudRouter

# TODO update the JSON string below
json = "{}"
# create an instance of GCPCloudRouter from a JSON string
gcp_cloud_router_instance = GCPCloudRouter.from_json(json)
# print the JSON string representation of the object
print(GCPCloudRouter.to_json())

# convert the object into a dict
gcp_cloud_router_dict = gcp_cloud_router_instance.to_dict()
# create an instance of GCPCloudRouter from a dict
gcp_cloud_router_from_dict = GCPCloudRouter.from_dict(gcp_cloud_router_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


