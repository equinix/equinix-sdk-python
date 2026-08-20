# LoaActionSearchFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[LoaActionFilter]**](LoaActionFilter.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.loa_action_search_filters import LoaActionSearchFilters

# TODO update the JSON string below
json = "{}"
# create an instance of LoaActionSearchFilters from a JSON string
loa_action_search_filters_instance = LoaActionSearchFilters.from_json(json)
# print the JSON string representation of the object
print(LoaActionSearchFilters.to_json())

# convert the object into a dict
loa_action_search_filters_dict = loa_action_search_filters_instance.to_dict()
# create an instance of LoaActionSearchFilters from a dict
loa_action_search_filters_from_dict = LoaActionSearchFilters.from_dict(loa_action_search_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


