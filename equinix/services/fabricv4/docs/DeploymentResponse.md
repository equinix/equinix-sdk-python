# DeploymentResponse

This API provides capability to retrieve user's deployments The response contains the details of the deployment including its state, topology, and providers. The deployment is identified by its UUID. The response also includes a list of notifications preferences for deployment status changes.     The response is in JSON format and follows the OpenAPI specification. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**topology** | [**DeploymentTopology**](DeploymentTopology.md) |  | [optional] 
**providers** | [**List[ProviderResponse]**](ProviderResponse.md) |  | [optional] 
**notifications** | [**List[SimplifiedNotification]**](SimplifiedNotification.md) | Preferences for notifications on deployement status changes | [optional] 

## Example

```python
from equinix.services.fabricv4.models.deployment_response import DeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentResponse from a JSON string
deployment_response_instance = DeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(DeploymentResponse.to_json())

# convert the object into a dict
deployment_response_dict = deployment_response_instance.to_dict()
# create an instance of DeploymentResponse from a dict
deployment_response_from_dict = DeploymentResponse.from_dict(deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


