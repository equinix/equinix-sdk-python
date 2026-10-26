# CrossConnectZSideResponseDemarcationPoint

Z-Side demarcation point. <br> cageUniqueSpaceId and cabinetUniqueSpaceId identify the Z-Side space. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patch_panel_id** | **str** | Patch Panel Identifier. | [optional] 
**patch_panel_port_a** | **int** | Specify the desired port number. When ports are not provided, next available ports will be used.  | [optional] 
**patch_panel_port_b** | **int** | Specify the desired port number. When ports are not provided, next available ports will be used. Required for Connector type FC and ST only.  | [optional] 
**connector_type** | **str** | Connector Type. | [optional] 
**cage_unique_space_id** | **str** | Unique identifier of the Cage. | [optional] [readonly] 
**cabinet_unique_space_id** | **str** | Unique identifier of the Cabinet. | [optional] [readonly] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_z_side_response_demarcation_point import CrossConnectZSideResponseDemarcationPoint

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectZSideResponseDemarcationPoint from a JSON string
cross_connect_z_side_response_demarcation_point_instance = CrossConnectZSideResponseDemarcationPoint.from_json(json)
# print the JSON string representation of the object
print(CrossConnectZSideResponseDemarcationPoint.to_json())

# convert the object into a dict
cross_connect_z_side_response_demarcation_point_dict = cross_connect_z_side_response_demarcation_point_instance.to_dict()
# create an instance of CrossConnectZSideResponseDemarcationPoint from a dict
cross_connect_z_side_response_demarcation_point_from_dict = CrossConnectZSideResponseDemarcationPoint.from_dict(cross_connect_z_side_response_demarcation_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


