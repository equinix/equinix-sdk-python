# InterconnectionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**interconnections** | [**List[Interconnection]**](Interconnection.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from equinix_metal.models.interconnection_list import InterconnectionList

# TODO update the JSON string below
json = "{}"
# create an instance of InterconnectionList from a JSON string
interconnection_list_instance = InterconnectionList.from_json(json)
# print the JSON string representation of the object
print(InterconnectionList.to_json())

# convert the object into a dict
interconnection_list_dict = interconnection_list_instance.to_dict()
# create an instance of InterconnectionList from a dict
interconnection_list_form_dict = interconnection_list.from_dict(interconnection_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


