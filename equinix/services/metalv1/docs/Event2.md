# Event2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**interpolated** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**modified_by** | **object** |  | [optional] 
**relationships** | [**List[Href]**](Href.md) |  | [optional] 
**state** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from equinix.services.metalv1.models.event2 import Event2

# TODO update the JSON string below
json = "{}"
# create an instance of Event2 from a JSON string
event2_instance = Event2.from_json(json)
# print the JSON string representation of the object
print(Event2.to_json())

# convert the object into a dict
event2_dict = event2_instance.to_dict()
# create an instance of Event2 from a dict
event2_from_dict = Event2.from_dict(event2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


