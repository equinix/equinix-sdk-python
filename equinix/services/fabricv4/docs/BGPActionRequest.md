# BGPActionRequest

BGP action request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**BGPActions**](BGPActions.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.bgp_action_request import BGPActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BGPActionRequest from a JSON string
bgp_action_request_instance = BGPActionRequest.from_json(json)
# print the JSON string representation of the object
print(BGPActionRequest.to_json())

# convert the object into a dict
bgp_action_request_dict = bgp_action_request_instance.to_dict()
# create an instance of BGPActionRequest from a dict
bgp_action_request_form_dict = bgp_action_request.from_dict(bgp_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


