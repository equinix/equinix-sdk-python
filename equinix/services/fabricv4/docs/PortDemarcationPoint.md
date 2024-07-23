# PortDemarcationPoint

Customer physical Port

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cabinet_unique_space_id** | **str** | Port cabinet unique space id | [optional] 
**cage_unique_space_id** | **str** | Port cage unique space id | [optional] 
**patch_panel** | **str** | Port patch panel | [optional] 
**patch_panel_name** | **str** | Port patch panel | [optional] 
**patch_panel_port_a** | **str** | Port patch panel port A | [optional] 
**patch_panel_port_b** | **str** | Port patch panel port B | [optional] 
**connector_type** | **str** | Port connector type | [optional] 
**ibx** | **str** | Port ibx identifier | [optional] 

## Example

```python
from equinix.services.fabricv4.models.port_demarcation_point import PortDemarcationPoint

# TODO update the JSON string below
json = "{}"
# create an instance of PortDemarcationPoint from a JSON string
port_demarcation_point_instance = PortDemarcationPoint.from_json(json)
# print the JSON string representation of the object
print(PortDemarcationPoint.to_json())

# convert the object into a dict
port_demarcation_point_dict = port_demarcation_point_instance.to_dict()
# create an instance of PortDemarcationPoint from a dict
port_demarcation_point_form_dict = port_demarcation_point.from_dict(port_demarcation_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


