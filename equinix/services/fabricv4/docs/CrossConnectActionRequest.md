# CrossConnectActionRequest

Cross Connect Action Request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CrossConnectActionType**](CrossConnectActionType.md) |  | 
**data** | [**CrossConnectActionData**](CrossConnectActionData.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_action_request import CrossConnectActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectActionRequest from a JSON string
cross_connect_action_request_instance = CrossConnectActionRequest.from_json(json)
# print the JSON string representation of the object
print(CrossConnectActionRequest.to_json())

# convert the object into a dict
cross_connect_action_request_dict = cross_connect_action_request_instance.to_dict()
# create an instance of CrossConnectActionRequest from a dict
cross_connect_action_request_from_dict = CrossConnectActionRequest.from_dict(cross_connect_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


