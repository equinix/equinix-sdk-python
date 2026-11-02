# CrossConnectResponse

Cross Connect Response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Cross Connect URI. | [optional] 
**type** | [**CrossConnectType**](CrossConnectType.md) |  | [optional] 
**uuid** | **str** | Cross Connect Identifier. | [optional] 
**name** | **str** | A short, descriptive name for this Cross Connect. | [optional] 
**state** | [**CrossConnectState**](CrossConnectState.md) |  | [optional] 
**allowed_actions** | [**List[CrossConnectResponseAllowedActionsInner]**](CrossConnectResponseAllowedActionsInner.md) | List of actions that can be performed on the Cross Connect based on its current state. Use these values to determine which action types are valid to submit to the actions endpoint.  | [optional] [readonly] 
**bmmr_type** | [**BmmrType**](BmmrType.md) |  | [optional] 
**media_type** | **str** | Media type of the Cross Connect. | [optional] 
**media_sub_type** | **str** | Media sub-type of the Cross Connect. | [optional] 
**circuit_id** | **str** | Circuit identifier of the Cross Connect. | [optional] 
**serial_number** | **str** | Serial number of the Cross Connect. | [optional] [readonly] 
**redundancy** | [**CrossConnectRedundancy**](CrossConnectRedundancy.md) |  | [optional] 
**a_side** | [**CrossConnectASideResponse**](CrossConnectASideResponse.md) |  | [optional] 
**z_side** | [**CrossConnectZSideResponse**](CrossConnectZSideResponse.md) |  | [optional] 
**account** | [**CrossConnectAccount**](CrossConnectAccount.md) |  | [optional] 
**notifications** | [**List[CrossConnectNotification]**](CrossConnectNotification.md) | Preferences for notifications on Cross Connect configuration or status changes.  | [optional] 
**order** | [**OrderResponse**](OrderResponse.md) |  | [optional] 
**links** | [**List[CrossConnectLink]**](CrossConnectLink.md) | Links to the Cross Connect sub-resources - schedules, services, notes and attachments.  | [optional] [readonly] 
**change_log** | [**CrossConnectChangelog**](CrossConnectChangelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_response import CrossConnectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectResponse from a JSON string
cross_connect_response_instance = CrossConnectResponse.from_json(json)
# print the JSON string representation of the object
print(CrossConnectResponse.to_json())

# convert the object into a dict
cross_connect_response_dict = cross_connect_response_instance.to_dict()
# create an instance of CrossConnectResponse from a dict
cross_connect_response_from_dict = CrossConnectResponse.from_dict(cross_connect_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


