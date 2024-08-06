# ConnectionActionRequest

Connection action request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**Actions**](Actions.md) |  | 
**description** | **str** | Connection rejection reason datail | [optional] 
**data** | [**ConnectionAcceptanceData**](ConnectionAcceptanceData.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connection_action_request import ConnectionActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionActionRequest from a JSON string
connection_action_request_instance = ConnectionActionRequest.from_json(json)
# print the JSON string representation of the object
print(ConnectionActionRequest.to_json())

# convert the object into a dict
connection_action_request_dict = connection_action_request_instance.to_dict()
# create an instance of ConnectionActionRequest from a dict
connection_action_request_from_dict = ConnectionActionRequest.from_dict(connection_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


