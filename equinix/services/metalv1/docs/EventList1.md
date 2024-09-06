# EventList1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[Event]**](Event.md) |  | [optional] 
**href** | **str** |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from equinix.services.metalv1.models.event_list1 import EventList1

# TODO update the JSON string below
json = "{}"
# create an instance of EventList1 from a JSON string
event_list1_instance = EventList1.from_json(json)
# print the JSON string representation of the object
print(EventList1.to_json())

# convert the object into a dict
event_list1_dict = event_list1_instance.to_dict()
# create an instance of EventList1 from a dict
event_list1_from_dict = EventList1.from_dict(event_list1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


