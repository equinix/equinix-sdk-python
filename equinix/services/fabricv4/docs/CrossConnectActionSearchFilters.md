# CrossConnectActionSearchFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[CrossConnectActionFilter]**](CrossConnectActionFilter.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_action_search_filters import CrossConnectActionSearchFilters

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectActionSearchFilters from a JSON string
cross_connect_action_search_filters_instance = CrossConnectActionSearchFilters.from_json(json)
# print the JSON string representation of the object
print(CrossConnectActionSearchFilters.to_json())

# convert the object into a dict
cross_connect_action_search_filters_dict = cross_connect_action_search_filters_instance.to_dict()
# create an instance of CrossConnectActionSearchFilters from a dict
cross_connect_action_search_filters_from_dict = CrossConnectActionSearchFilters.from_dict(cross_connect_action_search_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


