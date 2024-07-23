# LinkProtocolConnection

Connection details of Link Protocol

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Connection URI | [optional] [readonly] 
**uuid** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**bandwidth** | **int** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.link_protocol_connection import LinkProtocolConnection

# TODO update the JSON string below
json = "{}"
# create an instance of LinkProtocolConnection from a JSON string
link_protocol_connection_instance = LinkProtocolConnection.from_json(json)
# print the JSON string representation of the object
print(LinkProtocolConnection.to_json())

# convert the object into a dict
link_protocol_connection_dict = link_protocol_connection_instance.to_dict()
# create an instance of LinkProtocolConnection from a dict
link_protocol_connection_form_dict = link_protocol_connection.from_dict(link_protocol_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


