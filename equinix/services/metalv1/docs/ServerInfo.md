# ServerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**metro** | **str** | The metro ID or code to check the capacity in. | [optional] 
**plan** | **str** | The plan ID or slug to check the capacity of. | [optional] 
**quantity** | **str** | The number of servers to check the capacity of. | [optional] 

## Example

```python
from equinix_metal.models.server_info import ServerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ServerInfo from a JSON string
server_info_instance = ServerInfo.from_json(json)
# print the JSON string representation of the object
print(ServerInfo.to_json())

# convert the object into a dict
server_info_dict = server_info_instance.to_dict()
# create an instance of ServerInfo from a dict
server_info_form_dict = server_info.from_dict(server_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


