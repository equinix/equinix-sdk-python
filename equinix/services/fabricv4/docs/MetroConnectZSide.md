# MetroConnectZSide

Metro Connection ZSide configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patch_panel** | [**MetroConnectPatchPanel**](MetroConnectPatchPanel.md) |  | [optional] 
**loas** | [**List[PortLoa]**](PortLoa.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.metro_connect_z_side import MetroConnectZSide

# TODO update the JSON string below
json = "{}"
# create an instance of MetroConnectZSide from a JSON string
metro_connect_z_side_instance = MetroConnectZSide.from_json(json)
# print the JSON string representation of the object
print(MetroConnectZSide.to_json())

# convert the object into a dict
metro_connect_z_side_dict = metro_connect_z_side_instance.to_dict()
# create an instance of MetroConnectZSide from a dict
metro_connect_z_side_from_dict = MetroConnectZSide.from_dict(metro_connect_z_side_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


