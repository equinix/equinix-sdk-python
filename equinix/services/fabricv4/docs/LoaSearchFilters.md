# LoaSearchFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[LoaFilter]**](LoaFilter.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.loa_search_filters import LoaSearchFilters

# TODO update the JSON string below
json = "{}"
# create an instance of LoaSearchFilters from a JSON string
loa_search_filters_instance = LoaSearchFilters.from_json(json)
# print the JSON string representation of the object
print(LoaSearchFilters.to_json())

# convert the object into a dict
loa_search_filters_dict = loa_search_filters_instance.to_dict()
# create an instance of LoaSearchFilters from a dict
loa_search_filters_from_dict = LoaSearchFilters.from_dict(loa_search_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


