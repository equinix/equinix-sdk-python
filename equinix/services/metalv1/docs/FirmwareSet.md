# FirmwareSet

Represents a Firmware Set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[Attribute]**](Attribute.md) | Represents a list of attributes | [optional] 
**component_firmware** | [**List[Component]**](Component.md) | List of components versions | [optional] 
**created_at** | **datetime** | Datetime when the block was created. | [optional] [readonly] 
**href** | **str** |  | [optional] 
**name** | **str** | Firmware Set Name | [readonly] 
**updated_at** | **datetime** | Datetime when the block was updated. | [optional] [readonly] 
**uuid** | **str** | Firmware Set UUID | [readonly] 

## Example

```python
from equinix_metal.models.firmware_set import FirmwareSet

# TODO update the JSON string below
json = "{}"
# create an instance of FirmwareSet from a JSON string
firmware_set_instance = FirmwareSet.from_json(json)
# print the JSON string representation of the object
print(FirmwareSet.to_json())

# convert the object into a dict
firmware_set_dict = firmware_set_instance.to_dict()
# create an instance of FirmwareSet from a dict
firmware_set_form_dict = firmware_set.from_dict(firmware_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


