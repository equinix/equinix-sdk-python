# VirtualConnectionTimeServiceResponse

Fabric Connection Precision Time Service Response Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Connection URI | [readonly] 
**type** | **str** | Connection Type. | 
**uuid** | **str** | Connection UUID. | 
**a_side** | [**VirtualConnectionSide**](VirtualConnectionSide.md) |  | [optional] 
**z_side** | [**VirtualConnectionSide**](VirtualConnectionSide.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.virtual_connection_time_service_response import VirtualConnectionTimeServiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualConnectionTimeServiceResponse from a JSON string
virtual_connection_time_service_response_instance = VirtualConnectionTimeServiceResponse.from_json(json)
# print the JSON string representation of the object
print(VirtualConnectionTimeServiceResponse.to_json())

# convert the object into a dict
virtual_connection_time_service_response_dict = virtual_connection_time_service_response_instance.to_dict()
# create an instance of VirtualConnectionTimeServiceResponse from a dict
virtual_connection_time_service_response_from_dict = VirtualConnectionTimeServiceResponse.from_dict(virtual_connection_time_service_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


