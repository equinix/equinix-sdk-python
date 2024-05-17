# PlanSpecsCpusInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**href** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.plan_specs_cpus_inner import PlanSpecsCpusInner

# TODO update the JSON string below
json = "{}"
# create an instance of PlanSpecsCpusInner from a JSON string
plan_specs_cpus_inner_instance = PlanSpecsCpusInner.from_json(json)
# print the JSON string representation of the object
print(PlanSpecsCpusInner.to_json())

# convert the object into a dict
plan_specs_cpus_inner_dict = plan_specs_cpus_inner_instance.to_dict()
# create an instance of PlanSpecsCpusInner from a dict
plan_specs_cpus_inner_form_dict = plan_specs_cpus_inner.from_dict(plan_specs_cpus_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


