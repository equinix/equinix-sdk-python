# CapacityCheckPerMetroList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**servers** | [**List[CapacityCheckPerMetroInfo]**](CapacityCheckPerMetroInfo.md) |  | [optional] 

## Example

```python
from equinix_metal.models.capacity_check_per_metro_list import CapacityCheckPerMetroList

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityCheckPerMetroList from a JSON string
capacity_check_per_metro_list_instance = CapacityCheckPerMetroList.from_json(json)
# print the JSON string representation of the object
print(CapacityCheckPerMetroList.to_json())

# convert the object into a dict
capacity_check_per_metro_list_dict = capacity_check_per_metro_list_instance.to_dict()
# create an instance of CapacityCheckPerMetroList from a dict
capacity_check_per_metro_list_form_dict = capacity_check_per_metro_list.from_dict(capacity_check_per_metro_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


