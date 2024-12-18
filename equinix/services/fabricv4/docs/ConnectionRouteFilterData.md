# ConnectionRouteFilterData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Route filter URI | [optional] 
**type** | [**ConnectionRouteFilterDataType**](ConnectionRouteFilterDataType.md) |  | [optional] 
**uuid** | **str** | Route Filter identifier | [optional] 
**attachment_status** | [**ConnectionRouteAggregationDataAttachmentStatus**](ConnectionRouteAggregationDataAttachmentStatus.md) |  | [optional] 
**direction** | [**ConnectionRouteFilterDataDirection**](ConnectionRouteFilterDataDirection.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connection_route_filter_data import ConnectionRouteFilterData

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionRouteFilterData from a JSON string
connection_route_filter_data_instance = ConnectionRouteFilterData.from_json(json)
# print the JSON string representation of the object
print(ConnectionRouteFilterData.to_json())

# convert the object into a dict
connection_route_filter_data_dict = connection_route_filter_data_instance.to_dict()
# create an instance of ConnectionRouteFilterData from a dict
connection_route_filter_data_form_dict = connection_route_filter_data.from_dict(connection_route_filter_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


