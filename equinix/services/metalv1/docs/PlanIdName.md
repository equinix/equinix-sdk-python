# PlanIdName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.plan_id_name import PlanIdName

# TODO update the JSON string below
json = "{}"
# create an instance of PlanIdName from a JSON string
plan_id_name_instance = PlanIdName.from_json(json)
# print the JSON string representation of the object
print(PlanIdName.to_json())

# convert the object into a dict
plan_id_name_dict = plan_id_name_instance.to_dict()
# create an instance of PlanIdName from a dict
plan_id_name_form_dict = plan_id_name.from_dict(plan_id_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


