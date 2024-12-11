# RouteAggregationConnectionsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Connection URI | [optional] 
**type** | [**ConnectionType**](ConnectionType.md) |  | [optional] 
**uuid** | **str** | Route Aggregation identifier | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_aggregation_connections_data import RouteAggregationConnectionsData

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationConnectionsData from a JSON string
route_aggregation_connections_data_instance = RouteAggregationConnectionsData.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationConnectionsData.to_json())

# convert the object into a dict
route_aggregation_connections_data_dict = route_aggregation_connections_data_instance.to_dict()
# create an instance of RouteAggregationConnectionsData from a dict
route_aggregation_connections_data_form_dict = route_aggregation_connections_data.from_dict(route_aggregation_connections_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


