# MetroConnectZSideResponse

Metro Connection ZSide configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patch_panel** | [**MetroConnectPatchPanel**](MetroConnectPatchPanel.md) |  | [optional] 
**port** | [**MetroConnectPort**](MetroConnectPort.md) |  | [optional] 
**loas** | [**List[PortLoa]**](PortLoa.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.metro_connect_z_side_response import MetroConnectZSideResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MetroConnectZSideResponse from a JSON string
metro_connect_z_side_response_instance = MetroConnectZSideResponse.from_json(json)
# print the JSON string representation of the object
print(MetroConnectZSideResponse.to_json())

# convert the object into a dict
metro_connect_z_side_response_dict = metro_connect_z_side_response_instance.to_dict()
# create an instance of MetroConnectZSideResponse from a dict
metro_connect_z_side_response_from_dict = MetroConnectZSideResponse.from_dict(metro_connect_z_side_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


