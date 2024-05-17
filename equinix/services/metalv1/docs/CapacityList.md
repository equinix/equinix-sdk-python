# CapacityList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **Dict[str, Dict[str, CapacityLevelPerBaremetal]]** |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.capacity_list import CapacityList

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityList from a JSON string
capacity_list_instance = CapacityList.from_json(json)
# print the JSON string representation of the object
print(CapacityList.to_json())

# convert the object into a dict
capacity_list_dict = capacity_list_instance.to_dict()
# create an instance of CapacityList from a dict
capacity_list_form_dict = capacity_list.from_dict(capacity_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


