# Event1


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
from equinix.services.metalv1.models.event1 import Event1

# TODO update the JSON string below
json = "{}"
# create an instance of Event1 from a JSON string
event1_instance = Event1.from_json(json)
# print the JSON string representation of the object
print(Event1.to_json())

# convert the object into a dict
event1_dict = event1_instance.to_dict()
# create an instance of Event1 from a dict
event1_from_dict = Event1.from_dict(event1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


