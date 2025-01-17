# ConnectionLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**type** | [**ConnectionLinkType**](ConnectionLinkType.md) |  | [optional] 
**uuid** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connection_link import ConnectionLink

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionLink from a JSON string
connection_link_instance = ConnectionLink.from_json(json)
# print the JSON string representation of the object
print(ConnectionLink.to_json())

# convert the object into a dict
connection_link_dict = connection_link_instance.to_dict()
# create an instance of ConnectionLink from a dict
connection_link_from_dict = ConnectionLink.from_dict(connection_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


