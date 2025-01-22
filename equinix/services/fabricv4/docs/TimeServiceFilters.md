# TimeServiceFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[TimeServiceFilter]**](TimeServiceFilter.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.time_service_filters import TimeServiceFilters

# TODO update the JSON string below
json = "{}"
# create an instance of TimeServiceFilters from a JSON string
time_service_filters_instance = TimeServiceFilters.from_json(json)
# print the JSON string representation of the object
print(TimeServiceFilters.to_json())

# convert the object into a dict
time_service_filters_dict = time_service_filters_instance.to_dict()
# create an instance of TimeServiceFilters from a dict
time_service_filters_from_dict = TimeServiceFilters.from_dict(time_service_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


