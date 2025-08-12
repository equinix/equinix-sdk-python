# ClientInterfaces


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from equinix.services.fabricv4.models.client_interfaces import ClientInterfaces

# TODO update the JSON string below
json = "{}"
# create an instance of ClientInterfaces from a JSON string
client_interfaces_instance = ClientInterfaces.from_json(json)
# print the JSON string representation of the object
print(ClientInterfaces.to_json())

# convert the object into a dict
client_interfaces_dict = client_interfaces_instance.to_dict()
# create an instance of ClientInterfaces from a dict
client_interfaces_from_dict = ClientInterfaces.from_dict(client_interfaces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


