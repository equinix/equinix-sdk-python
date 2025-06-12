# DeploymentExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[DeploymentSearchExpressions]**](DeploymentSearchExpressions.md) |  | [optional] 
**var_or** | [**List[DeploymentSearchExpressions]**](DeploymentSearchExpressions.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.deployment_expression import DeploymentExpression

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentExpression from a JSON string
deployment_expression_instance = DeploymentExpression.from_json(json)
# print the JSON string representation of the object
print(DeploymentExpression.to_json())

# convert the object into a dict
deployment_expression_dict = deployment_expression_instance.to_dict()
# create an instance of DeploymentExpression from a dict
deployment_expression_from_dict = DeploymentExpression.from_dict(deployment_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


