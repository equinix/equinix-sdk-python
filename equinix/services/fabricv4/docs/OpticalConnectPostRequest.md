# OpticalConnectPostRequest

Request to order a single connection. The A-side is always a patch panel         port in your own cage; the Z-side shape depends on         connectionDestinationType.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**OpticalConnectPostRequestType**](OpticalConnectPostRequestType.md) |  | 
**bandwidth** | **int** | Connection bandwidth Mbps. &lt;br&gt; Available bandwidths depend on the IBX pair. &lt;br&gt; 1000 - 1 Gbps. &lt;br&gt; 10000 - 10 Gbps. &lt;br&gt; 100000 - 100 Gbps. &lt;br&gt;  | 
**connection_destination_type** | [**OpticalConnectPostRequestConnectionDestinationType**](OpticalConnectPostRequestConnectionDestinationType.md) |  | 
**path_type** | [**OpticalConnectPostRequestPathType**](OpticalConnectPostRequestPathType.md) |  | 
**redundancy** | [**OpticalConnectRedundancy**](OpticalConnectRedundancy.md) |  | [optional] 
**a_side** | [**OpticalConnectASideRequest**](OpticalConnectASideRequest.md) |  | 
**z_side** | [**OpticalConnectZSideRequest**](OpticalConnectZSideRequest.md) |  | 
**order** | [**OpticalConnectOrder**](OpticalConnectOrder.md) |  | [optional] 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | [optional] 
**notifications** | [**List[OpticalConnectNotification]**](OpticalConnectNotification.md) | Contacts to notify about connection configuration and status changes | [optional] 
**bmmr_type** | [**OpticalConnectPostRequestBmmrType**](OpticalConnectPostRequestBmmrType.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.optical_connect_post_request import OpticalConnectPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OpticalConnectPostRequest from a JSON string
optical_connect_post_request_instance = OpticalConnectPostRequest.from_json(json)
# print the JSON string representation of the object
print(OpticalConnectPostRequest.to_json())

# convert the object into a dict
optical_connect_post_request_dict = optical_connect_post_request_instance.to_dict()
# create an instance of OpticalConnectPostRequest from a dict
optical_connect_post_request_from_dict = OpticalConnectPostRequest.from_dict(optical_connect_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


