# BGPActionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Routing Protocol URI | [optional] 
**uuid** | **str** | Routing protocol identifier | [optional] 
**type** | [**BGPActions**](BGPActions.md) |  | [optional] 
**description** | **str** | BGP action description | [optional] 
**state** | [**BGPActionStates**](BGPActionStates.md) |  | [optional] 
**changelog** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.bgp_action_data import BGPActionData

# TODO update the JSON string below
json = "{}"
# create an instance of BGPActionData from a JSON string
bgp_action_data_instance = BGPActionData.from_json(json)
# print the JSON string representation of the object
print(BGPActionData.to_json())

# convert the object into a dict
bgp_action_data_dict = bgp_action_data_instance.to_dict()
# create an instance of BGPActionData from a dict
bgp_action_data_from_dict = BGPActionData.from_dict(bgp_action_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


