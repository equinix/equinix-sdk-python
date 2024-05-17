# IPAssignmentMetro


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.ip_assignment_metro import IPAssignmentMetro

# TODO update the JSON string below
json = "{}"
# create an instance of IPAssignmentMetro from a JSON string
ip_assignment_metro_instance = IPAssignmentMetro.from_json(json)
# print the JSON string representation of the object
print(IPAssignmentMetro.to_json())

# convert the object into a dict
ip_assignment_metro_dict = ip_assignment_metro_instance.to_dict()
# create an instance of IPAssignmentMetro from a dict
ip_assignment_metro_form_dict = ip_assignment_metro.from_dict(ip_assignment_metro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


