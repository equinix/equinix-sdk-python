# DeploymentSearchExpressions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**SearchDeploymentField**](SearchDeploymentField.md) |  | [optional] 
**operator** | [**DeploymentSearchExpressionsOperator**](DeploymentSearchExpressionsOperator.md) |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.deployment_search_expressions import DeploymentSearchExpressions

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentSearchExpressions from a JSON string
deployment_search_expressions_instance = DeploymentSearchExpressions.from_json(json)
# print the JSON string representation of the object
print(DeploymentSearchExpressions.to_json())

# convert the object into a dict
deployment_search_expressions_dict = deployment_search_expressions_instance.to_dict()
# create an instance of DeploymentSearchExpressions from a dict
deployment_search_expressions_from_dict = DeploymentSearchExpressions.from_dict(deployment_search_expressions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


