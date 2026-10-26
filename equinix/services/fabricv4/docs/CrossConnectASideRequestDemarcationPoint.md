# CrossConnectASideRequestDemarcationPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patch_panel_id** | **str** | Patch Panel Identifier. | 
**patch_panel_port_a** | **int** | Specify the desired port number. When ports are not provided, next available ports will be used.  | [optional] 
**patch_panel_port_b** | **int** | Specify the desired port number. When ports are not provided, next available ports will be used. Required for Connector type FC and ST only.  | [optional] 
**connector_type** | **str** | Connector Type. | 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_a_side_request_demarcation_point import CrossConnectASideRequestDemarcationPoint

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectASideRequestDemarcationPoint from a JSON string
cross_connect_a_side_request_demarcation_point_instance = CrossConnectASideRequestDemarcationPoint.from_json(json)
# print the JSON string representation of the object
print(CrossConnectASideRequestDemarcationPoint.to_json())

# convert the object into a dict
cross_connect_a_side_request_demarcation_point_dict = cross_connect_a_side_request_demarcation_point_instance.to_dict()
# create an instance of CrossConnectASideRequestDemarcationPoint from a dict
cross_connect_a_side_request_demarcation_point_from_dict = CrossConnectASideRequestDemarcationPoint.from_dict(cross_connect_a_side_request_demarcation_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


