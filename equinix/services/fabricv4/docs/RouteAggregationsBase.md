# RouteAggregationsBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RouteAggregationsBaseType**](RouteAggregationsBaseType.md) |  | 
**name** | **str** |  | 
**description** | **str** | Customer-provided connection description | [optional] 
**project** | [**Project**](Project.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.route_aggregations_base import RouteAggregationsBase

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationsBase from a JSON string
route_aggregations_base_instance = RouteAggregationsBase.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationsBase.to_json())

# convert the object into a dict
route_aggregations_base_dict = route_aggregations_base_instance.to_dict()
# create an instance of RouteAggregationsBase from a dict
route_aggregations_base_from_dict = RouteAggregationsBase.from_dict(route_aggregations_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


