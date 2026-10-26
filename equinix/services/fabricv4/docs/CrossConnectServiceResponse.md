# CrossConnectServiceResponse

Service ordered alongside the Cross Connect.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Service URI. | [optional] [readonly] 
**uuid** | **str** | Service Identifier. | [optional] [readonly] 
**type** | [**CrossConnectServiceType**](CrossConnectServiceType.md) |  | [optional] [readonly] 
**state** | [**CrossConnectServiceState**](CrossConnectServiceState.md) |  | [optional] [readonly] 
**device** | [**PatchEquipmentResponse**](PatchEquipmentResponse.md) | Patch equipment device details. Returned for the XC_PATCH_EQUIPMENT service. | [optional] [readonly] 
**description** | **str** | Additional notes captured for the service. | [optional] [readonly] 
**change_log** | [**CrossConnectChangelog**](CrossConnectChangelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_service_response import CrossConnectServiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectServiceResponse from a JSON string
cross_connect_service_response_instance = CrossConnectServiceResponse.from_json(json)
# print the JSON string representation of the object
print(CrossConnectServiceResponse.to_json())

# convert the object into a dict
cross_connect_service_response_dict = cross_connect_service_response_instance.to_dict()
# create an instance of CrossConnectServiceResponse from a dict
cross_connect_service_response_from_dict = CrossConnectServiceResponse.from_dict(cross_connect_service_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


