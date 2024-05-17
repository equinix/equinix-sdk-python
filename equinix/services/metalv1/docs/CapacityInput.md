# CapacityInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**servers** | [**List[ServerInfo]**](ServerInfo.md) |  | [optional] 

## Example

```python
from equinix_metal.models.capacity_input import CapacityInput

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityInput from a JSON string
capacity_input_instance = CapacityInput.from_json(json)
# print the JSON string representation of the object
print(CapacityInput.to_json())

# convert the object into a dict
capacity_input_dict = capacity_input_instance.to_dict()
# create an instance of CapacityInput from a dict
capacity_input_form_dict = capacity_input.from_dict(capacity_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


