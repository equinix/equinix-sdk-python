# ConnectionRouteAggregationData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Route Aggregation URI | [optional] 
**type** | [**ConnectionRouteAggregationDataType**](ConnectionRouteAggregationDataType.md) |  | [optional] 
**uuid** | **str** | Route Aggregation identifier | [optional] 
**attachment_status** | [**ConnectionRouteAggregationDataAttachmentStatus**](ConnectionRouteAggregationDataAttachmentStatus.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connection_route_aggregation_data import ConnectionRouteAggregationData

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionRouteAggregationData from a JSON string
connection_route_aggregation_data_instance = ConnectionRouteAggregationData.from_json(json)
# print the JSON string representation of the object
print(ConnectionRouteAggregationData.to_json())

# convert the object into a dict
connection_route_aggregation_data_dict = connection_route_aggregation_data_instance.to_dict()
# create an instance of ConnectionRouteAggregationData from a dict
connection_route_aggregation_data_form_dict = connection_route_aggregation_data.from_dict(connection_route_aggregation_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


