# PhysicalPortSettings

Physical Port configuration settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** |  | [optional] 
**package_type** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.physical_port_settings import PhysicalPortSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalPortSettings from a JSON string
physical_port_settings_instance = PhysicalPortSettings.from_json(json)
# print the JSON string representation of the object
print(PhysicalPortSettings.to_json())

# convert the object into a dict
physical_port_settings_dict = physical_port_settings_instance.to_dict()
# create an instance of PhysicalPortSettings from a dict
physical_port_settings_from_dict = PhysicalPortSettings.from_dict(physical_port_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


