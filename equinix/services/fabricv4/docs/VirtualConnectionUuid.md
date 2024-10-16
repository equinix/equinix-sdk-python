# VirtualConnectionUuid

UUID of the Fabric Connection Instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Connection URI | [optional] [readonly] 
**type** | **str** | Connection Type | [optional] 
**uuid** | **str** | Connection UUID. | 

## Example

```python
from equinix.services.fabricv4.models.virtual_connection_uuid import VirtualConnectionUuid

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualConnectionUuid from a JSON string
virtual_connection_uuid_instance = VirtualConnectionUuid.from_json(json)
# print the JSON string representation of the object
print(VirtualConnectionUuid.to_json())

# convert the object into a dict
virtual_connection_uuid_dict = virtual_connection_uuid_instance.to_dict()
# create an instance of VirtualConnectionUuid from a dict
virtual_connection_uuid_form_dict = virtual_connection_uuid.from_dict(virtual_connection_uuid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


