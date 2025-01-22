# VirtualConnectionSide

Fabric Connection access point object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_point** | [**AccessPoint**](AccessPoint.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.virtual_connection_side import VirtualConnectionSide

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualConnectionSide from a JSON string
virtual_connection_side_instance = VirtualConnectionSide.from_json(json)
# print the JSON string representation of the object
print(VirtualConnectionSide.to_json())

# convert the object into a dict
virtual_connection_side_dict = virtual_connection_side_instance.to_dict()
# create an instance of VirtualConnectionSide from a dict
virtual_connection_side_from_dict = VirtualConnectionSide.from_dict(virtual_connection_side_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


