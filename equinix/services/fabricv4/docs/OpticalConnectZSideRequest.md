# OpticalConnectZSideRequest

Z-Side configuration. <br> For COLO, specify the destination patch panel and ports. <br> For BMMR and REMOTE, specify the location and Letter of Authorization. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**demarcation_point** | [**OpticalConnectDemarcationPoint**](OpticalConnectDemarcationPoint.md) |  | [optional] 
**location** | [**OpticalConnectLocation**](OpticalConnectLocation.md) |  | [optional] 
**loa** | [**OpticalConnectLOA**](OpticalConnectLOA.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.optical_connect_z_side_request import OpticalConnectZSideRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OpticalConnectZSideRequest from a JSON string
optical_connect_z_side_request_instance = OpticalConnectZSideRequest.from_json(json)
# print the JSON string representation of the object
print(OpticalConnectZSideRequest.to_json())

# convert the object into a dict
optical_connect_z_side_request_dict = optical_connect_z_side_request_instance.to_dict()
# create an instance of OpticalConnectZSideRequest from a dict
optical_connect_z_side_request_from_dict = OpticalConnectZSideRequest.from_dict(optical_connect_z_side_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


