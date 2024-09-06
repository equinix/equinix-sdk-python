# OperatingSystemList1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**operating_systems** | [**List[OperatingSystem]**](OperatingSystem.md) |  | [optional] 

## Example

```python
from equinix.services.metalv1.models.operating_system_list1 import OperatingSystemList1

# TODO update the JSON string below
json = "{}"
# create an instance of OperatingSystemList1 from a JSON string
operating_system_list1_instance = OperatingSystemList1.from_json(json)
# print the JSON string representation of the object
print(OperatingSystemList1.to_json())

# convert the object into a dict
operating_system_list1_dict = operating_system_list1_instance.to_dict()
# create an instance of OperatingSystemList1 from a dict
operating_system_list1_from_dict = OperatingSystemList1.from_dict(operating_system_list1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


