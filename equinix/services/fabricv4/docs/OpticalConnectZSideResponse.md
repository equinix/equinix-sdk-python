# OpticalConnectZSideResponse

Terminating end as provisioned, with the demarcation point and IBX location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**demarcation_point** | [**OpticalConnectResponseDemarcationPoint**](OpticalConnectResponseDemarcationPoint.md) |  | [optional] 
**location** | [**OpticalConnectLocation**](OpticalConnectLocation.md) |  | [optional] 
**loa** | [**OpticalConnectLOA**](OpticalConnectLOA.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.optical_connect_z_side_response import OpticalConnectZSideResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OpticalConnectZSideResponse from a JSON string
optical_connect_z_side_response_instance = OpticalConnectZSideResponse.from_json(json)
# print the JSON string representation of the object
print(OpticalConnectZSideResponse.to_json())

# convert the object into a dict
optical_connect_z_side_response_dict = optical_connect_z_side_response_instance.to_dict()
# create an instance of OpticalConnectZSideResponse from a dict
optical_connect_z_side_response_from_dict = OpticalConnectZSideResponse.from_dict(optical_connect_z_side_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


