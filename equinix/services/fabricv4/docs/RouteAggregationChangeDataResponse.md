# RouteAggregationChangeDataResponse

List of Route Aggregation changes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[RouteAggregationChangeData]**](RouteAggregationChangeData.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_aggregation_change_data_response import RouteAggregationChangeDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationChangeDataResponse from a JSON string
route_aggregation_change_data_response_instance = RouteAggregationChangeDataResponse.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationChangeDataResponse.to_json())

# convert the object into a dict
route_aggregation_change_data_response_dict = route_aggregation_change_data_response_instance.to_dict()
# create an instance of RouteAggregationChangeDataResponse from a dict
route_aggregation_change_data_response_form_dict = route_aggregation_change_data_response.from_dict(route_aggregation_change_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


