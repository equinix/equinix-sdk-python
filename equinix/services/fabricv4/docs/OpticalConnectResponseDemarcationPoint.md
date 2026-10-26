# OpticalConnectResponseDemarcationPoint

Demarcation point as provisioned, with the cage and cabinet it belongs to. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patch_panel_id** | **str** | Unique identifier of the patch panel. | [optional] 
**patch_panel_port_a** | **str** | Specify the desired port number for Port A. &lt;br&gt; When ports are not provided, next available ports will be used.  | [optional] 
**patch_panel_port_b** | **str** | Specify the desired port number for Port B. &lt;br&gt; When ports are not provided, next available ports will be used. &lt;br&gt; Required for Connector type FC, SC and ST only.  | [optional] 
**connector_type** | [**OpticalConnectDemarcationPointConnectorType**](OpticalConnectDemarcationPointConnectorType.md) |  | [optional] 
**cage_unique_space_id** | **str** | Unique identifier of the cage. | [optional] 
**cabinet_unique_space_id** | **str** | Unique identifier of the cabinet. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.optical_connect_response_demarcation_point import OpticalConnectResponseDemarcationPoint

# TODO update the JSON string below
json = "{}"
# create an instance of OpticalConnectResponseDemarcationPoint from a JSON string
optical_connect_response_demarcation_point_instance = OpticalConnectResponseDemarcationPoint.from_json(json)
# print the JSON string representation of the object
print(OpticalConnectResponseDemarcationPoint.to_json())

# convert the object into a dict
optical_connect_response_demarcation_point_dict = optical_connect_response_demarcation_point_instance.to_dict()
# create an instance of OpticalConnectResponseDemarcationPoint from a dict
optical_connect_response_demarcation_point_from_dict = OpticalConnectResponseDemarcationPoint.from_dict(optical_connect_response_demarcation_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


