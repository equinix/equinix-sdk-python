# MessagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Role of the message sender user or assistant | [optional] 
**content** | **str** | Content of the chat message | [optional] 

## Example

```python
from equinix.services.fabricv4.models.messages_inner import MessagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MessagesInner from a JSON string
messages_inner_instance = MessagesInner.from_json(json)
# print the JSON string representation of the object
print(MessagesInner.to_json())

# convert the object into a dict
messages_inner_dict = messages_inner_instance.to_dict()
# create an instance of MessagesInner from a dict
messages_inner_from_dict = MessagesInner.from_dict(messages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


