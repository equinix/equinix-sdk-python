# CapacityLevelPerBaremetal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**level** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.capacity_level_per_baremetal import CapacityLevelPerBaremetal

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityLevelPerBaremetal from a JSON string
capacity_level_per_baremetal_instance = CapacityLevelPerBaremetal.from_json(json)
# print the JSON string representation of the object
print(CapacityLevelPerBaremetal.to_json())

# convert the object into a dict
capacity_level_per_baremetal_dict = capacity_level_per_baremetal_instance.to_dict()
# create an instance of CapacityLevelPerBaremetal from a dict
capacity_level_per_baremetal_form_dict = capacity_level_per_baremetal.from_dict(capacity_level_per_baremetal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


