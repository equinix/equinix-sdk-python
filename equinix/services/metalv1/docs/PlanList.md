# PlanList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**plans** | [**List[Plan]**](Plan.md) |  | [optional] 

## Example

```python
from equinix_metal.models.plan_list import PlanList

# TODO update the JSON string below
json = "{}"
# create an instance of PlanList from a JSON string
plan_list_instance = PlanList.from_json(json)
# print the JSON string representation of the object
print(PlanList.to_json())

# convert the object into a dict
plan_list_dict = plan_list_instance.to_dict()
# create an instance of PlanList from a dict
plan_list_form_dict = plan_list.from_dict(plan_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


