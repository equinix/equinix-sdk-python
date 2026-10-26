# LiveEventFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[LiveEventSimpleExpression]**](LiveEventSimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.live_event_filters import LiveEventFilters

# TODO update the JSON string below
json = "{}"
# create an instance of LiveEventFilters from a JSON string
live_event_filters_instance = LiveEventFilters.from_json(json)
# print the JSON string representation of the object
print(LiveEventFilters.to_json())

# convert the object into a dict
live_event_filters_dict = live_event_filters_instance.to_dict()
# create an instance of LiveEventFilters from a dict
live_event_filters_from_dict = LiveEventFilters.from_dict(live_event_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


