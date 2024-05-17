# PlanSpecsFeatures


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**raid** | **bool** |  | [optional] 
**txt** | **bool** |  | [optional] 
**uefi** | **bool** |  | [optional] 

## Example

```python
from equinix_metal.models.plan_specs_features import PlanSpecsFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of PlanSpecsFeatures from a JSON string
plan_specs_features_instance = PlanSpecsFeatures.from_json(json)
# print the JSON string representation of the object
print(PlanSpecsFeatures.to_json())

# convert the object into a dict
plan_specs_features_dict = plan_specs_features_instance.to_dict()
# create an instance of PlanSpecsFeatures from a dict
plan_specs_features_form_dict = plan_specs_features.from_dict(plan_specs_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


