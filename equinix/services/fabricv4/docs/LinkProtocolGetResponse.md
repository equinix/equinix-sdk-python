# LinkProtocolGetResponse

List of Vlans

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[LinkProtocolResponse]**](LinkProtocolResponse.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.link_protocol_get_response import LinkProtocolGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LinkProtocolGetResponse from a JSON string
link_protocol_get_response_instance = LinkProtocolGetResponse.from_json(json)
# print the JSON string representation of the object
print(LinkProtocolGetResponse.to_json())

# convert the object into a dict
link_protocol_get_response_dict = link_protocol_get_response_instance.to_dict()
# create an instance of LinkProtocolGetResponse from a dict
link_protocol_get_response_form_dict = link_protocol_get_response.from_dict(link_protocol_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


