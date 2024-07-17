# RouteFilterConnectionsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Connection URI | [optional] 
**type** | [**ConnectionType**](ConnectionType.md) |  | [optional] 
**uuid** | **str** | Route Filter identifier | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_filter_connections_data import RouteFilterConnectionsData

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFilterConnectionsData from a JSON string
route_filter_connections_data_instance = RouteFilterConnectionsData.from_json(json)
# print the JSON string representation of the object
print(RouteFilterConnectionsData.to_json())

# convert the object into a dict
route_filter_connections_data_dict = route_filter_connections_data_instance.to_dict()
# create an instance of RouteFilterConnectionsData from a dict
route_filter_connections_data_form_dict = route_filter_connections_data.from_dict(route_filter_connections_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


