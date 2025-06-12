# Deployment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**topology** | [**DeploymentTopology**](DeploymentTopology.md) |  | [optional] 
**providers** | [**List[OrchestratorProviders]**](OrchestratorProviders.md) |  | 
**project** | [**Project**](Project.md) |  | 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | 
**order** | [**Order**](Order.md) |  | [optional] 
**notifications** | [**List[SimplifiedNotification]**](SimplifiedNotification.md) | Preferences for notifications on deployement status changes | [optional] 

## Example

```python
from equinix.services.fabricv4.models.deployment import Deployment

# TODO update the JSON string below
json = "{}"
# create an instance of Deployment from a JSON string
deployment_instance = Deployment.from_json(json)
# print the JSON string representation of the object
print(Deployment.to_json())

# convert the object into a dict
deployment_dict = deployment_instance.to_dict()
# create an instance of Deployment from a dict
deployment_from_dict = Deployment.from_dict(deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


