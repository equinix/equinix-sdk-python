# TopUtilizedStatistics

This API provides service-level traffic metrics for the top utilized ports so that you can view access and gather key information required to manage service subscription sizing and capacity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[Statistics]**](Statistics.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.top_utilized_statistics import TopUtilizedStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of TopUtilizedStatistics from a JSON string
top_utilized_statistics_instance = TopUtilizedStatistics.from_json(json)
# print the JSON string representation of the object
print(TopUtilizedStatistics.to_json())

# convert the object into a dict
top_utilized_statistics_dict = top_utilized_statistics_instance.to_dict()
# create an instance of TopUtilizedStatistics from a dict
top_utilized_statistics_from_dict = TopUtilizedStatistics.from_dict(top_utilized_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


