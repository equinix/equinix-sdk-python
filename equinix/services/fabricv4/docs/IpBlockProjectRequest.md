# IpBlockProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | project id | 

## Example

```python
from equinix.services.fabricv4.models.ip_block_project_request import IpBlockProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IpBlockProjectRequest from a JSON string
ip_block_project_request_instance = IpBlockProjectRequest.from_json(json)
# print the JSON string representation of the object
print(IpBlockProjectRequest.to_json())

# convert the object into a dict
ip_block_project_request_dict = ip_block_project_request_instance.to_dict()
# create an instance of IpBlockProjectRequest from a dict
ip_block_project_request_from_dict = IpBlockProjectRequest.from_dict(ip_block_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


