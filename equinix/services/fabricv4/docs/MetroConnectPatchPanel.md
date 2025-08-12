# MetroConnectPatchPanel

Patch panel object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Patch Panel ID | [optional] 
**port_a** | **str** | Patch Panel Port A | [optional] 
**port_b** | **str** | Patch Panel Port B | [optional] 
**connector_type** | **str** | Type of Connector | [optional] 
**cage_unique_space_id** | **str** | Cage Unique Space Id | [optional] 
**cabinet_unique_space_id** | **str** | Cabinet Unique Space Id | [optional] 
**ibx** | **str** | IBX identifier | [optional] 

## Example

```python
from equinix.services.fabricv4.models.metro_connect_patch_panel import MetroConnectPatchPanel

# TODO update the JSON string below
json = "{}"
# create an instance of MetroConnectPatchPanel from a JSON string
metro_connect_patch_panel_instance = MetroConnectPatchPanel.from_json(json)
# print the JSON string representation of the object
print(MetroConnectPatchPanel.to_json())

# convert the object into a dict
metro_connect_patch_panel_dict = metro_connect_patch_panel_instance.to_dict()
# create an instance of MetroConnectPatchPanel from a dict
metro_connect_patch_panel_from_dict = MetroConnectPatchPanel.from_dict(metro_connect_patch_panel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


