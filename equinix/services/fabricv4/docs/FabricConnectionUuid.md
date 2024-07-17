# FabricConnectionUuid

UUID of the Fabric Connection Instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | uuid of the Fabric L2 connection | 
**href** | **str** | the href for the L2 connection | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.fabric_connection_uuid import FabricConnectionUuid

# TODO update the JSON string below
json = "{}"
# create an instance of FabricConnectionUuid from a JSON string
fabric_connection_uuid_instance = FabricConnectionUuid.from_json(json)
# print the JSON string representation of the object
print(FabricConnectionUuid.to_json())

# convert the object into a dict
fabric_connection_uuid_dict = fabric_connection_uuid_instance.to_dict()
# create an instance of FabricConnectionUuid from a dict
fabric_connection_uuid_form_dict = fabric_connection_uuid.from_dict(fabric_connection_uuid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


