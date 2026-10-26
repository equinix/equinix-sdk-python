# CrossConnectSearchFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[CrossConnectFilter]**](CrossConnectFilter.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_search_filters import CrossConnectSearchFilters

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectSearchFilters from a JSON string
cross_connect_search_filters_instance = CrossConnectSearchFilters.from_json(json)
# print the JSON string representation of the object
print(CrossConnectSearchFilters.to_json())

# convert the object into a dict
cross_connect_search_filters_dict = cross_connect_search_filters_instance.to_dict()
# create an instance of CrossConnectSearchFilters from a dict
cross_connect_search_filters_from_dict = CrossConnectSearchFilters.from_dict(cross_connect_search_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


