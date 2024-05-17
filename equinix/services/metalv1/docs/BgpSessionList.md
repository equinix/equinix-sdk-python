# BgpSessionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_sessions** | [**List[BgpSession]**](BgpSession.md) |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.bgp_session_list import BgpSessionList

# TODO update the JSON string below
json = "{}"
# create an instance of BgpSessionList from a JSON string
bgp_session_list_instance = BgpSessionList.from_json(json)
# print the JSON string representation of the object
print(BgpSessionList.to_json())

# convert the object into a dict
bgp_session_list_dict = bgp_session_list_instance.to_dict()
# create an instance of BgpSessionList from a dict
bgp_session_list_form_dict = bgp_session_list.from_dict(bgp_session_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


