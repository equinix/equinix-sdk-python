# MetricsSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**MetricFilters**](MetricFilters.md) |  | 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.metrics_search_request import MetricsSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsSearchRequest from a JSON string
metrics_search_request_instance = MetricsSearchRequest.from_json(json)
# print the JSON string representation of the object
print(MetricsSearchRequest.to_json())

# convert the object into a dict
metrics_search_request_dict = metrics_search_request_instance.to_dict()
# create an instance of MetricsSearchRequest from a dict
metrics_search_request_from_dict = MetricsSearchRequest.from_dict(metrics_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


