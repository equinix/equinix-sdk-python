# PlanSpecs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpus** | [**List[PlanSpecsCpusInner]**](PlanSpecsCpusInner.md) |  | [optional] 
**drives** | [**List[PlanSpecsDrivesInner]**](PlanSpecsDrivesInner.md) |  | [optional] 
**features** | [**PlanSpecsFeatures**](PlanSpecsFeatures.md) |  | [optional] 
**href** | **str** |  | [optional] 
**memory** | [**PlanSpecsMemory**](PlanSpecsMemory.md) |  | [optional] 
**nics** | [**List[PlanSpecsNicsInner]**](PlanSpecsNicsInner.md) |  | [optional] 

## Example

```python
from equinix_metal.models.plan_specs import PlanSpecs

# TODO update the JSON string below
json = "{}"
# create an instance of PlanSpecs from a JSON string
plan_specs_instance = PlanSpecs.from_json(json)
# print the JSON string representation of the object
print(PlanSpecs.to_json())

# convert the object into a dict
plan_specs_dict = plan_specs_instance.to_dict()
# create an instance of PlanSpecs from a dict
plan_specs_form_dict = plan_specs.from_dict(plan_specs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


