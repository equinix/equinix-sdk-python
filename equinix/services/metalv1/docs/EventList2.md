# EventList2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[Event]**](Event.md) |  | [optional] 
**href** | **str** |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from equinix.services.metalv1.models.event_list2 import EventList2

# TODO update the JSON string below
json = "{}"
# create an instance of EventList2 from a JSON string
event_list2_instance = EventList2.from_json(json)
# print the JSON string representation of the object
print(EventList2.to_json())

# convert the object into a dict
event_list2_dict = event_list2_instance.to_dict()
# create an instance of EventList2 from a dict
event_list2_from_dict = EventList2.from_dict(event_list2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


