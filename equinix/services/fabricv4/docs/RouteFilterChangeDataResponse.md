# RouteFilterChangeDataResponse

List of route filter changes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[RouteFilterChangeData]**](RouteFilterChangeData.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_filter_change_data_response import RouteFilterChangeDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFilterChangeDataResponse from a JSON string
route_filter_change_data_response_instance = RouteFilterChangeDataResponse.from_json(json)
# print the JSON string representation of the object
print(RouteFilterChangeDataResponse.to_json())

# convert the object into a dict
route_filter_change_data_response_dict = route_filter_change_data_response_instance.to_dict()
# create an instance of RouteFilterChangeDataResponse from a dict
route_filter_change_data_response_from_dict = RouteFilterChangeDataResponse.from_dict(route_filter_change_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


