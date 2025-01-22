# LinkProtocolServiceToken

Service Token details of Link Protocol

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Service Token URI | [optional] [readonly] 
**uuid** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**bandwidth** | **int** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.link_protocol_service_token import LinkProtocolServiceToken

# TODO update the JSON string below
json = "{}"
# create an instance of LinkProtocolServiceToken from a JSON string
link_protocol_service_token_instance = LinkProtocolServiceToken.from_json(json)
# print the JSON string representation of the object
print(LinkProtocolServiceToken.to_json())

# convert the object into a dict
link_protocol_service_token_dict = link_protocol_service_token_instance.to_dict()
# create an instance of LinkProtocolServiceToken from a dict
link_protocol_service_token_from_dict = LinkProtocolServiceToken.from_dict(link_protocol_service_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


