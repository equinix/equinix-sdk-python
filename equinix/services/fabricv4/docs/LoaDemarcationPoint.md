# LoaDemarcationPoint

Specifies the demarcation point. <br> For CAGE_LOA - cageUniqueSpaceId is required. <br> For PATCH_PANEL_LOA - patchPanelId is required. <br> For PATCH_PANEL_PORT_LOA - patchPanelId, patchPanelPortA, patchPanelPortB      and connectorType is required. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cage_unique_space_id** | **str** | Unique identifier of the Cage. | [optional] 
**patch_panel_id** | **str** | Unique identifier of the Patch Panel.  | [optional] 
**patch_panel_port_a** | **int** | Specify the desired port number. &lt;br&gt; When ports are not provided, next available ports will be used.  | [optional] 
**patch_panel_port_b** | **int** | Specify the desired port number. &lt;br&gt; When ports are not provided, next available ports will be used. &lt;br&gt; Required for Connector type FC and ST only.  | [optional] 
**connector_type** | [**LoaPatchPanelConnectorType**](LoaPatchPanelConnectorType.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.loa_demarcation_point import LoaDemarcationPoint

# TODO update the JSON string below
json = "{}"
# create an instance of LoaDemarcationPoint from a JSON string
loa_demarcation_point_instance = LoaDemarcationPoint.from_json(json)
# print the JSON string representation of the object
print(LoaDemarcationPoint.to_json())

# convert the object into a dict
loa_demarcation_point_dict = loa_demarcation_point_instance.to_dict()
# create an instance of LoaDemarcationPoint from a dict
loa_demarcation_point_from_dict = LoaDemarcationPoint.from_dict(loa_demarcation_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


