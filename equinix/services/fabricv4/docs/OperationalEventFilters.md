# OperationalEventFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[OperationalEventSimpleExpression]**](OperationalEventSimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.operational_event_filters import OperationalEventFilters

# TODO update the JSON string below
json = "{}"
# create an instance of OperationalEventFilters from a JSON string
operational_event_filters_instance = OperationalEventFilters.from_json(json)
# print the JSON string representation of the object
print(OperationalEventFilters.to_json())

# convert the object into a dict
operational_event_filters_dict = operational_event_filters_instance.to_dict()
# create an instance of OperationalEventFilters from a dict
operational_event_filters_from_dict = OperationalEventFilters.from_dict(operational_event_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


