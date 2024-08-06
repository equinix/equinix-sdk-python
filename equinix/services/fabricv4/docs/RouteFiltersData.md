# RouteFiltersData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Route Filter URI | [optional] 
**type** | [**ConnectionRouteFilterDataType**](ConnectionRouteFilterDataType.md) |  | [optional] 
**uuid** | **str** | Route Filter identifier | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** | Customer-provided connection description | [optional] 
**state** | [**RouteFilterState**](RouteFilterState.md) |  | [optional] 
**change** | [**RouteFiltersChange**](RouteFiltersChange.md) |  | [optional] 
**not_matched_rule_action** | [**RouteFiltersDataNotMatchedRuleAction**](RouteFiltersDataNotMatchedRuleAction.md) |  | [optional] 
**connections_count** | **int** |  | [optional] 
**rules_count** | **int** |  | [optional] 
**project** | [**RouteFiltersDataProject**](RouteFiltersDataProject.md) |  | [optional] 
**changelog** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_filters_data import RouteFiltersData

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFiltersData from a JSON string
route_filters_data_instance = RouteFiltersData.from_json(json)
# print the JSON string representation of the object
print(RouteFiltersData.to_json())

# convert the object into a dict
route_filters_data_dict = route_filters_data_instance.to_dict()
# create an instance of RouteFiltersData from a dict
route_filters_data_from_dict = RouteFiltersData.from_dict(route_filters_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


