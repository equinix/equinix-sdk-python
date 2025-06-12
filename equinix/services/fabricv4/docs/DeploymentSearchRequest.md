# DeploymentSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**DeploymentExpression**](DeploymentExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.deployment_search_request import DeploymentSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentSearchRequest from a JSON string
deployment_search_request_instance = DeploymentSearchRequest.from_json(json)
# print the JSON string representation of the object
print(DeploymentSearchRequest.to_json())

# convert the object into a dict
deployment_search_request_dict = deployment_search_request_instance.to_dict()
# create an instance of DeploymentSearchRequest from a dict
deployment_search_request_from_dict = DeploymentSearchRequest.from_dict(deployment_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


