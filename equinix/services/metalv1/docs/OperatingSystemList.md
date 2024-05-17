# OperatingSystemList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**operating_systems** | [**List[OperatingSystem]**](OperatingSystem.md) |  | [optional] 

## Example

```python
from equinix_metal.models.operating_system_list import OperatingSystemList

# TODO update the JSON string below
json = "{}"
# create an instance of OperatingSystemList from a JSON string
operating_system_list_instance = OperatingSystemList.from_json(json)
# print the JSON string representation of the object
print(OperatingSystemList.to_json())

# convert the object into a dict
operating_system_list_dict = operating_system_list_instance.to_dict()
# create an instance of OperatingSystemList from a dict
operating_system_list_form_dict = operating_system_list.from_dict(operating_system_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


