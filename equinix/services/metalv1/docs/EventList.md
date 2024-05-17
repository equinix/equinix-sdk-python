# EventList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[Event]**](Event.md) |  | [optional] 
**href** | **str** |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from equinix_metal.models.event_list import EventList

# TODO update the JSON string below
json = "{}"
# create an instance of EventList from a JSON string
event_list_instance = EventList.from_json(json)
# print the JSON string representation of the object
print(EventList.to_json())

# convert the object into a dict
event_list_dict = event_list_instance.to_dict()
# create an instance of EventList from a dict
event_list_form_dict = event_list.from_dict(event_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


