# PortSettings

Port configuration settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyout** | **bool** |  | [optional] 
**view_port_permission** | **bool** |  | [optional] 
**place_vc_order_permission** | **bool** |  | [optional] 
**layer3_enabled** | **bool** |  | [optional] 
**shared_port_type** | **bool** |  | [optional] 
**shared_port_product** | [**PortSettingsSharedPortProduct**](PortSettingsSharedPortProduct.md) |  | [optional] 
**package_type** | [**PortSettingsPackageType**](PortSettingsPackageType.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.port_settings import PortSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PortSettings from a JSON string
port_settings_instance = PortSettings.from_json(json)
# print the JSON string representation of the object
print(PortSettings.to_json())

# convert the object into a dict
port_settings_dict = port_settings_instance.to_dict()
# create an instance of PortSettings from a dict
port_settings_form_dict = port_settings.from_dict(port_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


