# OpticalConnectASideRequest

A-Side configuration. Always a patch panel port from your cage. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patch_panel_id** | **str** | Unique identifier of the patch panel. | [optional] 
**patch_panel_port_a** | **str** | Specify the desired port number for Port A. &lt;br&gt; When ports are not provided, next available ports will be used.  | [optional] 
**patch_panel_port_b** | **str** | Specify the desired port number for Port B. &lt;br&gt; When ports are not provided, next available ports will be used. &lt;br&gt; Required for Connector type FC, SC and ST only.  | [optional] 
**connector_type** | [**OpticalConnectPatchPanelFieldsConnectorType**](OpticalConnectPatchPanelFieldsConnectorType.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.optical_connect_a_side_request import OpticalConnectASideRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OpticalConnectASideRequest from a JSON string
optical_connect_a_side_request_instance = OpticalConnectASideRequest.from_json(json)
# print the JSON string representation of the object
print(OpticalConnectASideRequest.to_json())

# convert the object into a dict
optical_connect_a_side_request_dict = optical_connect_a_side_request_instance.to_dict()
# create an instance of OpticalConnectASideRequest from a dict
optical_connect_a_side_request_from_dict = OpticalConnectASideRequest.from_dict(optical_connect_a_side_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


