# OpticalConnectASideRequest

A-Side configuration. Always a patch panel port from your cage. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**demarcation_point** | [**OpticalConnectDemarcationPoint**](OpticalConnectDemarcationPoint.md) |  | [optional] 

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


