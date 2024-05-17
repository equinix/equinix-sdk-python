# PlanSpecsDrivesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**count** | **int** |  | [optional] 
**href** | **str** |  | [optional] 
**size** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.plan_specs_drives_inner import PlanSpecsDrivesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PlanSpecsDrivesInner from a JSON string
plan_specs_drives_inner_instance = PlanSpecsDrivesInner.from_json(json)
# print the JSON string representation of the object
print(PlanSpecsDrivesInner.to_json())

# convert the object into a dict
plan_specs_drives_inner_dict = plan_specs_drives_inner_instance.to_dict()
# create an instance of PlanSpecsDrivesInner from a dict
plan_specs_drives_inner_form_dict = plan_specs_drives_inner.from_dict(plan_specs_drives_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


