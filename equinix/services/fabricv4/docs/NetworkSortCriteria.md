# NetworkSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**NetworkSortDirection**](NetworkSortDirection.md) |  | [optional] 
**var_property** | [**NetworkSortBy**](NetworkSortBy.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.network_sort_criteria import NetworkSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkSortCriteria from a JSON string
network_sort_criteria_instance = NetworkSortCriteria.from_json(json)
# print the JSON string representation of the object
print(NetworkSortCriteria.to_json())

# convert the object into a dict
network_sort_criteria_dict = network_sort_criteria_instance.to_dict()
# create an instance of NetworkSortCriteria from a dict
network_sort_criteria_form_dict = network_sort_criteria.from_dict(network_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


