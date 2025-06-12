# DeploymentSearchResponse

A list of deployments matching the search criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DeploymentResponse]**](DeploymentResponse.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.deployment_search_response import DeploymentSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentSearchResponse from a JSON string
deployment_search_response_instance = DeploymentSearchResponse.from_json(json)
# print the JSON string representation of the object
print(DeploymentSearchResponse.to_json())

# convert the object into a dict
deployment_search_response_dict = deployment_search_response_instance.to_dict()
# create an instance of DeploymentSearchResponse from a dict
deployment_search_response_from_dict = DeploymentSearchResponse.from_dict(deployment_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


