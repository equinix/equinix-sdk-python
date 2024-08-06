# CloudRouterChangeOperation

Fabric Cloud Router change operation data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**ServiceTokenChangeOperationOp**](ServiceTokenChangeOperationOp.md) |  | 
**path** | **str** | path inside document leading to updated parameter | 
**value** | **object** | new value for updated parameter | 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_change_operation import CloudRouterChangeOperation

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterChangeOperation from a JSON string
cloud_router_change_operation_instance = CloudRouterChangeOperation.from_json(json)
# print the JSON string representation of the object
print(CloudRouterChangeOperation.to_json())

# convert the object into a dict
cloud_router_change_operation_dict = cloud_router_change_operation_instance.to_dict()
# create an instance of CloudRouterChangeOperation from a dict
cloud_router_change_operation_from_dict = CloudRouterChangeOperation.from_dict(cloud_router_change_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


