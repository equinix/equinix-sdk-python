# PlanAvailableInMetrosInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | href to the Metro | [optional] 
**price** | [**PlanAvailableInInnerPrice**](PlanAvailableInInnerPrice.md) |  | [optional] 

## Example

```python
from equinix_metal.models.plan_available_in_metros_inner import PlanAvailableInMetrosInner

# TODO update the JSON string below
json = "{}"
# create an instance of PlanAvailableInMetrosInner from a JSON string
plan_available_in_metros_inner_instance = PlanAvailableInMetrosInner.from_json(json)
# print the JSON string representation of the object
print(PlanAvailableInMetrosInner.to_json())

# convert the object into a dict
plan_available_in_metros_inner_dict = plan_available_in_metros_inner_instance.to_dict()
# create an instance of PlanAvailableInMetrosInner from a dict
plan_available_in_metros_inner_form_dict = plan_available_in_metros_inner.from_dict(plan_available_in_metros_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


