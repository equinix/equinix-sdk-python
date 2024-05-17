# InterconnectionMetroList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 
**metros** | [**List[InterconnectionMetroListMetrosInner]**](InterconnectionMetroListMetrosInner.md) |  | [optional] 

## Example

```python
from equinix_metal.models.interconnection_metro_list import InterconnectionMetroList

# TODO update the JSON string below
json = "{}"
# create an instance of InterconnectionMetroList from a JSON string
interconnection_metro_list_instance = InterconnectionMetroList.from_json(json)
# print the JSON string representation of the object
print(InterconnectionMetroList.to_json())

# convert the object into a dict
interconnection_metro_list_dict = interconnection_metro_list_instance.to_dict()
# create an instance of InterconnectionMetroList from a dict
interconnection_metro_list_form_dict = interconnection_metro_list.from_dict(interconnection_metro_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


