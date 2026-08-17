# OpticalConnectPatchPanelFields

Patch Panel configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patch_panel_id** | **str** | Unique identifier of the patch panel. | [optional] 
**patch_panel_port_a** | **str** | Specify the desired port number for Port A. &lt;br&gt; When ports are not provided, next available ports will be used.  | [optional] 
**patch_panel_port_b** | **str** | Specify the desired port number for Port B. &lt;br&gt; When ports are not provided, next available ports will be used. &lt;br&gt; Required for Connector type FC, SC and ST only.  | [optional] 
**connector_type** | [**OpticalConnectPatchPanelFieldsConnectorType**](OpticalConnectPatchPanelFieldsConnectorType.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.optical_connect_patch_panel_fields import OpticalConnectPatchPanelFields

# TODO update the JSON string below
json = "{}"
# create an instance of OpticalConnectPatchPanelFields from a JSON string
optical_connect_patch_panel_fields_instance = OpticalConnectPatchPanelFields.from_json(json)
# print the JSON string representation of the object
print(OpticalConnectPatchPanelFields.to_json())

# convert the object into a dict
optical_connect_patch_panel_fields_dict = optical_connect_patch_panel_fields_instance.to_dict()
# create an instance of OpticalConnectPatchPanelFields from a dict
optical_connect_patch_panel_fields_from_dict = OpticalConnectPatchPanelFields.from_dict(optical_connect_patch_panel_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


