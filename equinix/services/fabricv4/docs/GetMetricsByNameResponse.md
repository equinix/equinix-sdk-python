# GetMetricsByNameResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[Metric]**](Metric.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.get_metrics_by_name_response import GetMetricsByNameResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMetricsByNameResponse from a JSON string
get_metrics_by_name_response_instance = GetMetricsByNameResponse.from_json(json)
# print the JSON string representation of the object
print(GetMetricsByNameResponse.to_json())

# convert the object into a dict
get_metrics_by_name_response_dict = get_metrics_by_name_response_instance.to_dict()
# create an instance of GetMetricsByNameResponse from a dict
get_metrics_by_name_response_from_dict = GetMetricsByNameResponse.from_dict(get_metrics_by_name_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


