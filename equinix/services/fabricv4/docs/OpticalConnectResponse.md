# OpticalConnectResponse

Optical Metro Connect connection with its current state and the resolved         physical termination points at both ends.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | URI of this Optical Connect resource. | [optional] [readonly] 
**uuid** | **str** | Unique identifier of this Optical Connect. | [optional] [readonly] 
**type** | [**OpticalConnectResponseType**](OpticalConnectResponseType.md) |  | [optional] 
**name** | **str** | Equinix-assigned name, derived from the account number and the two IBX locations.  | [optional] [readonly] 
**state** | [**OpticalConnectState**](OpticalConnectState.md) |  | [optional] 
**bandwidth** | **int** | Provisioned connection bandwidth in Mbps. | [optional] 
**connection_destination_type** | [**OpticalConnectResponseConnectionDestinationType**](OpticalConnectResponseConnectionDestinationType.md) |  | [optional] 
**path_type** | [**OpticalConnectResponsePathType**](OpticalConnectResponsePathType.md) |  | [optional] 
**bmmr_type** | [**OpticalConnectResponseBmmrType**](OpticalConnectResponseBmmrType.md) |  | [optional] 
**redundancy** | [**OpticalConnectRedundancy**](OpticalConnectRedundancy.md) |  | [optional] 
**a_side** | [**OpticalConnectASideResponse**](OpticalConnectASideResponse.md) |  | [optional] 
**z_side** | [**OpticalConnectZSideResponse**](OpticalConnectZSideResponse.md) |  | [optional] 
**order** | [**OpticalConnectOrder**](OpticalConnectOrder.md) |  | [optional] 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | [optional] 
**notifications** | [**List[OpticalConnectNotification]**](OpticalConnectNotification.md) | Preferences for notifications on connection configuration or status changes | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.optical_connect_response import OpticalConnectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OpticalConnectResponse from a JSON string
optical_connect_response_instance = OpticalConnectResponse.from_json(json)
# print the JSON string representation of the object
print(OpticalConnectResponse.to_json())

# convert the object into a dict
optical_connect_response_dict = optical_connect_response_instance.to_dict()
# create an instance of OpticalConnectResponse from a dict
optical_connect_response_from_dict = OpticalConnectResponse.from_dict(optical_connect_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


