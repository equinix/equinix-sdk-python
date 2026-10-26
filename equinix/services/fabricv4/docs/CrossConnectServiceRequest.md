# CrossConnectServiceRequest

Service to order alongside the Cross Connect. <br> Send one entry per service. <br> device and description apply to the XC_PATCH_EQUIPMENT service only. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CrossConnectServiceType**](CrossConnectServiceType.md) |  | 
**device** | [**PatchEquipmentRequest**](PatchEquipmentRequest.md) | Patch equipment device details. Required for the XC_PATCH_EQUIPMENT service.  | [optional] 
**description** | **str** | Additional notes for the service. Required for the XC_PATCH_EQUIPMENT service.  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_service_request import CrossConnectServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectServiceRequest from a JSON string
cross_connect_service_request_instance = CrossConnectServiceRequest.from_json(json)
# print the JSON string representation of the object
print(CrossConnectServiceRequest.to_json())

# convert the object into a dict
cross_connect_service_request_dict = cross_connect_service_request_instance.to_dict()
# create an instance of CrossConnectServiceRequest from a dict
cross_connect_service_request_from_dict = CrossConnectServiceRequest.from_dict(cross_connect_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


