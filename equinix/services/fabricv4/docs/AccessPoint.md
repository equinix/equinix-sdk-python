# AccessPoint

Access point object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AccessPointType**](AccessPointType.md) |  | [optional] 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | [optional] 
**location** | [**SimplifiedLocation**](SimplifiedLocation.md) |  | [optional] 
**port** | [**SimplifiedPort**](SimplifiedPort.md) |  | [optional] 
**profile** | [**SimplifiedServiceProfile**](SimplifiedServiceProfile.md) |  | [optional] 
**router** | [**CloudRouter**](CloudRouter.md) |  | [optional] 
**link_protocol** | [**SimplifiedLinkProtocol**](SimplifiedLinkProtocol.md) |  | [optional] 
**virtual_device** | [**VirtualDevice**](VirtualDevice.md) |  | [optional] 
**interface** | [**Interface**](Interface.md) |  | [optional] 
**network** | [**SimplifiedNetwork**](SimplifiedNetwork.md) |  | [optional] 
**seller_region** | **str** | Access point seller region | [optional] 
**peering_type** | [**PeeringType**](PeeringType.md) |  | [optional] 
**authentication_key** | **str** | Access point authentication key | [optional] 
**provider_connection_id** | **str** | Provider assigned Connection Id | [optional] 
**virtual_network** | [**VirtualNetwork**](VirtualNetwork.md) |  | [optional] 
**interconnection** | [**MetalInterconnection**](MetalInterconnection.md) |  | [optional] 
**vpic_interface** | [**VpicInterface**](VpicInterface.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.access_point import AccessPoint

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPoint from a JSON string
access_point_instance = AccessPoint.from_json(json)
# print the JSON string representation of the object
print(AccessPoint.to_json())

# convert the object into a dict
access_point_dict = access_point_instance.to_dict()
# create an instance of AccessPoint from a dict
access_point_form_dict = access_point.from_dict(access_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


