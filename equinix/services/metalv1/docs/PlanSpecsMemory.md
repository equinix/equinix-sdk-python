# PlanSpecsMemory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**total** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.plan_specs_memory import PlanSpecsMemory

# TODO update the JSON string below
json = "{}"
# create an instance of PlanSpecsMemory from a JSON string
plan_specs_memory_instance = PlanSpecsMemory.from_json(json)
# print the JSON string representation of the object
print(PlanSpecsMemory.to_json())

# convert the object into a dict
plan_specs_memory_dict = plan_specs_memory_instance.to_dict()
# create an instance of PlanSpecsMemory from a dict
plan_specs_memory_form_dict = plan_specs_memory.from_dict(plan_specs_memory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


