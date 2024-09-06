# PlanList1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**plans** | [**List[Plan]**](Plan.md) |  | [optional] 

## Example

```python
from equinix.services.metalv1.models.plan_list1 import PlanList1

# TODO update the JSON string below
json = "{}"
# create an instance of PlanList1 from a JSON string
plan_list1_instance = PlanList1.from_json(json)
# print the JSON string representation of the object
print(PlanList1.to_json())

# convert the object into a dict
plan_list1_dict = plan_list1_instance.to_dict()
# create an instance of PlanList1 from a dict
plan_list1_from_dict = PlanList1.from_dict(plan_list1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


