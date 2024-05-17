# Plan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_in** | [**List[PlanAvailableInInner]**](PlanAvailableInInner.md) | Shows which facilities the plan is available in, and the facility-based price if it is different from the default price. | [optional] 
**available_in_metros** | [**List[PlanAvailableInMetrosInner]**](PlanAvailableInMetrosInner.md) | Shows which metros the plan is available in, and the metro-based price if it is different from the default price. | [optional] 
**categories** | **List[str]** | Categories of the plan, like compute or storage. A Plan can belong to multiple categories. | [optional] 
**var_class** | **str** |  | [optional] 
**deployment_types** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**legacy** | **bool** | Deprecated. Always return false | [optional] 
**line** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**pricing** | **object** |  | [optional] 
**slug** | **str** |  | [optional] 
**specs** | [**PlanSpecs**](PlanSpecs.md) |  | [optional] 
**type** | **str** | The plan type | [optional] 

## Example

```python
from equinix_metal.models.plan import Plan

# TODO update the JSON string below
json = "{}"
# create an instance of Plan from a JSON string
plan_instance = Plan.from_json(json)
# print the JSON string representation of the object
print(Plan.to_json())

# convert the object into a dict
plan_dict = plan_instance.to_dict()
# create an instance of Plan from a dict
plan_form_dict = plan.from_dict(plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


