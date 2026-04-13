# ToolCallInformationInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of tools called | [optional] 
**input** | **str** | Content of the tool request | [optional] 
**response** | **str** | Content of the tool response | [optional] 

## Example

```python
from equinix.services.fabricv4.models.tool_call_information_inner import ToolCallInformationInner

# TODO update the JSON string below
json = "{}"
# create an instance of ToolCallInformationInner from a JSON string
tool_call_information_inner_instance = ToolCallInformationInner.from_json(json)
# print the JSON string representation of the object
print(ToolCallInformationInner.to_json())

# convert the object into a dict
tool_call_information_inner_dict = tool_call_information_inner_instance.to_dict()
# create an instance of ToolCallInformationInner from a dict
tool_call_information_inner_from_dict = ToolCallInformationInner.from_dict(tool_call_information_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


