# AuthTokenProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backend_transfer_enabled** | **bool** |  | [optional] 
**bgp_config** | [**Href**](Href.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**customdata** | **object** |  | [optional] 
**devices** | [**List[Href]**](Href.md) |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**invitations** | [**List[Href]**](Href.md) |  | [optional] 
**max_devices** | **object** |  | [optional] 
**members** | [**List[Href]**](Href.md) |  | [optional] 
**memberships** | [**List[Href]**](Href.md) |  | [optional] 
**name** | **str** | The name of the project. Cannot contain characters encoded in greater than 3 bytes such as emojis. | [optional] 
**network_status** | **object** |  | [optional] 
**organization** | [**Href**](Href.md) |  | [optional] 
**payment_method** | [**Href**](Href.md) |  | [optional] 
**ssh_keys** | [**List[Href]**](Href.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**type** | **str** | The type of the project. Projects of type &#x60;vmce&#x60; are part of an in development feature and not available to all customers. | [optional] 
**updated_at** | **datetime** |  | [optional] 
**url** | **str** |  | [optional] 
**volumes** | [**List[Href]**](Href.md) |  | [optional] 

## Example

```python
from equinix_metal.models.auth_token_project import AuthTokenProject

# TODO update the JSON string below
json = "{}"
# create an instance of AuthTokenProject from a JSON string
auth_token_project_instance = AuthTokenProject.from_json(json)
# print the JSON string representation of the object
print(AuthTokenProject.to_json())

# convert the object into a dict
auth_token_project_dict = auth_token_project_instance.to_dict()
# create an instance of AuthTokenProject from a dict
auth_token_project_form_dict = auth_token_project.from_dict(auth_token_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


