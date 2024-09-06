# CapacityList1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **Dict[str, Dict[str, CapacityLevelPerBaremetal]]** |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix.services.metalv1.models.capacity_list1 import CapacityList1

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityList1 from a JSON string
capacity_list1_instance = CapacityList1.from_json(json)
# print the JSON string representation of the object
print(CapacityList1.to_json())

# convert the object into a dict
capacity_list1_dict = capacity_list1_instance.to_dict()
# create an instance of CapacityList1 from a dict
capacity_list1_from_dict = CapacityList1.from_dict(capacity_list1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


