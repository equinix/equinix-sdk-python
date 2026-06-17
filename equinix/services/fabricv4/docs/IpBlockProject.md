# IpBlockProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | URI of the project | [optional] 
**project_id** | **str** | project id | 

## Example

```python
from equinix.services.fabricv4.models.ip_block_project import IpBlockProject

# TODO update the JSON string below
json = "{}"
# create an instance of IpBlockProject from a JSON string
ip_block_project_instance = IpBlockProject.from_json(json)
# print the JSON string representation of the object
print(IpBlockProject.to_json())

# convert the object into a dict
ip_block_project_dict = ip_block_project_instance.to_dict()
# create an instance of IpBlockProject from a dict
ip_block_project_from_dict = IpBlockProject.from_dict(ip_block_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


