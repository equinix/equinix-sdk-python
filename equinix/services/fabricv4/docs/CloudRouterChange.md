# CloudRouterChange

Current state of latest CloudRouter change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Uniquely identifies a change | [optional] 
**type** | [**CloudRouterChangeType**](CloudRouterChangeType.md) |  | 
**status** | [**CloudRouterChangeStatus**](CloudRouterChangeStatus.md) |  | [optional] 
**created_date_time** | **datetime** | Set when change flow starts | [optional] 
**updated_date_time** | **datetime** | Set when change object is updated | 
**information** | **str** | Additional information | [optional] 
**data** | [**CloudRouterChangeOperation**](CloudRouterChangeOperation.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_change import CloudRouterChange

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterChange from a JSON string
cloud_router_change_instance = CloudRouterChange.from_json(json)
# print the JSON string representation of the object
print(CloudRouterChange.to_json())

# convert the object into a dict
cloud_router_change_dict = cloud_router_change_instance.to_dict()
# create an instance of CloudRouterChange from a dict
cloud_router_change_form_dict = cloud_router_change.from_dict(cloud_router_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


