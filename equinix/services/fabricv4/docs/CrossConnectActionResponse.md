# CrossConnectActionResponse

Cross Connect Action Response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Action URI. | [optional] [readonly] 
**uuid** | **str** | Action Identifier. | [optional] [readonly] 
**type** | [**CrossConnectActionType**](CrossConnectActionType.md) |  | [optional] [readonly] 
**state** | [**CrossConnectActionState**](CrossConnectActionState.md) |  | [optional] [readonly] 
**data** | [**CrossConnectActionResponseData**](CrossConnectActionResponseData.md) |  | [optional] [readonly] 
**change_log** | [**CrossConnectChangelog**](CrossConnectChangelog.md) |  | [optional] [readonly] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_action_response import CrossConnectActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectActionResponse from a JSON string
cross_connect_action_response_instance = CrossConnectActionResponse.from_json(json)
# print the JSON string representation of the object
print(CrossConnectActionResponse.to_json())

# convert the object into a dict
cross_connect_action_response_dict = cross_connect_action_response_instance.to_dict()
# create an instance of CrossConnectActionResponse from a dict
cross_connect_action_response_from_dict = CrossConnectActionResponse.from_dict(cross_connect_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


