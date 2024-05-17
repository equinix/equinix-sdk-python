# BGPSessionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_family** | **str** | Address family for BGP session. | [optional] 
**default_route** | **bool** | Set the default route policy. | [optional] [default to False]
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.bgp_session_input import BGPSessionInput

# TODO update the JSON string below
json = "{}"
# create an instance of BGPSessionInput from a JSON string
bgp_session_input_instance = BGPSessionInput.from_json(json)
# print the JSON string representation of the object
print(BGPSessionInput.to_json())

# convert the object into a dict
bgp_session_input_dict = bgp_session_input_instance.to_dict()
# create an instance of BGPSessionInput from a dict
bgp_session_input_form_dict = bgp_session_input.from_dict(bgp_session_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


