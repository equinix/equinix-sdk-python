# PlanSpecsNicsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**href** | **str** |  | [optional] 
**type** | **str** | Values may include &#39;1Gbps&#39;, &#39;10Gbps&#39;, &#39;25Gbps&#39; | [optional] 

## Example

```python
from equinix.services.metalv1.models.plan_specs_nics_inner import PlanSpecsNicsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PlanSpecsNicsInner from a JSON string
plan_specs_nics_inner_instance = PlanSpecsNicsInner.from_json(json)
# print the JSON string representation of the object
print(PlanSpecsNicsInner.to_json())

# convert the object into a dict
plan_specs_nics_inner_dict = plan_specs_nics_inner_instance.to_dict()
# create an instance of PlanSpecsNicsInner from a dict
plan_specs_nics_inner_from_dict = PlanSpecsNicsInner.from_dict(plan_specs_nics_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


