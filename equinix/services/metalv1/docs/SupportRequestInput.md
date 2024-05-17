# SupportRequestInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**message** | **str** |  | 
**priority** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**subject** | **str** |  | 

## Example

```python
from equinix_metal.models.support_request_input import SupportRequestInput

# TODO update the JSON string below
json = "{}"
# create an instance of SupportRequestInput from a JSON string
support_request_input_instance = SupportRequestInput.from_json(json)
# print the JSON string representation of the object
print(SupportRequestInput.to_json())

# convert the object into a dict
support_request_input_dict = support_request_input_instance.to_dict()
# create an instance of SupportRequestInput from a dict
support_request_input_form_dict = support_request_input.from_dict(support_request_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


