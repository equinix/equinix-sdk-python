# GCPPermission

Provides the GCP permission configuration for the orchestrator. This permission is used to manage the GCP resources and their access control. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AWSPermissionType**](AWSPermissionType.md) |  | 
**project_id** | **str** |  | 
**provider_id** | **str** |  | 
**pool_id** | **str** |  | 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.gcp_permission import GCPPermission

# TODO update the JSON string below
json = "{}"
# create an instance of GCPPermission from a JSON string
gcp_permission_instance = GCPPermission.from_json(json)
# print the JSON string representation of the object
print(GCPPermission.to_json())

# convert the object into a dict
gcp_permission_dict = gcp_permission_instance.to_dict()
# create an instance of GCPPermission from a dict
gcp_permission_from_dict = GCPPermission.from_dict(gcp_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


