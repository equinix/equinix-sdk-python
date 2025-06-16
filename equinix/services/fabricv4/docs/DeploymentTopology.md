# DeploymentTopology


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.deployment_topology import DeploymentTopology

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentTopology from a JSON string
deployment_topology_instance = DeploymentTopology.from_json(json)
# print the JSON string representation of the object
print(DeploymentTopology.to_json())

# convert the object into a dict
deployment_topology_dict = deployment_topology_instance.to_dict()
# create an instance of DeploymentTopology from a dict
deployment_topology_from_dict = DeploymentTopology.from_dict(deployment_topology_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


