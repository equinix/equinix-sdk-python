# RouteFilterChangeData

Current state of latest Route Filter change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Current outcome of the change flow | [optional] 
**created_by** | **str** | Created by User Key | [optional] 
**created_date_time** | **datetime** | Set when change flow starts | [optional] 
**updated_by** | **str** | Updated by User Key | [optional] 
**updated_date_time** | **datetime** | Set when change object is updated | [optional] 
**information** | **str** | Additional information | [optional] 
**data** | [**RouteFiltersChangeOperation**](RouteFiltersChangeOperation.md) |  | [optional] 
**uuid** | **str** | Uniquely identifies a change | 
**type** | [**RouteFiltersChangeType**](RouteFiltersChangeType.md) |  | 
**href** | **str** | Route Filter Change URI | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_filter_change_data import RouteFilterChangeData

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFilterChangeData from a JSON string
route_filter_change_data_instance = RouteFilterChangeData.from_json(json)
# print the JSON string representation of the object
print(RouteFilterChangeData.to_json())

# convert the object into a dict
route_filter_change_data_dict = route_filter_change_data_instance.to_dict()
# create an instance of RouteFilterChangeData from a dict
route_filter_change_data_from_dict = RouteFilterChangeData.from_dict(route_filter_change_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


