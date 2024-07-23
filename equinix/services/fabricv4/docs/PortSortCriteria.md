# PortSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**PortSortDirection**](PortSortDirection.md) |  | [optional] 
**var_property** | [**PortSortBy**](PortSortBy.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.port_sort_criteria import PortSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of PortSortCriteria from a JSON string
port_sort_criteria_instance = PortSortCriteria.from_json(json)
# print the JSON string representation of the object
print(PortSortCriteria.to_json())

# convert the object into a dict
port_sort_criteria_dict = port_sort_criteria_instance.to_dict()
# create an instance of PortSortCriteria from a dict
port_sort_criteria_form_dict = port_sort_criteria.from_dict(port_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


