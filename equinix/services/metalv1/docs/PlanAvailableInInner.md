# PlanAvailableInInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | href to the Facility | [optional] 
**price** | [**PlanAvailableInInnerPrice**](PlanAvailableInInnerPrice.md) |  | [optional] 

## Example

```python
from equinix.services.metalv1.models.plan_available_in_inner import PlanAvailableInInner

# TODO update the JSON string below
json = "{}"
# create an instance of PlanAvailableInInner from a JSON string
plan_available_in_inner_instance = PlanAvailableInInner.from_json(json)
# print the JSON string representation of the object
print(PlanAvailableInInner.to_json())

# convert the object into a dict
plan_available_in_inner_dict = plan_available_in_inner_instance.to_dict()
# create an instance of PlanAvailableInInner from a dict
plan_available_in_inner_from_dict = PlanAvailableInInner.from_dict(plan_available_in_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


