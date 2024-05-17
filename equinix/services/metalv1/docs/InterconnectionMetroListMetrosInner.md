# InterconnectionMetroListMetrosInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**providers** | [**List[InterconnectionMetroListMetrosInnerAllOfProvidersInner]**](InterconnectionMetroListMetrosInnerAllOfProvidersInner.md) | A list of providers and their equivalent regions available for connecting to the provider network. | [optional] 

## Example

```python
from equinix_metal.models.interconnection_metro_list_metros_inner import InterconnectionMetroListMetrosInner

# TODO update the JSON string below
json = "{}"
# create an instance of InterconnectionMetroListMetrosInner from a JSON string
interconnection_metro_list_metros_inner_instance = InterconnectionMetroListMetrosInner.from_json(json)
# print the JSON string representation of the object
print(InterconnectionMetroListMetrosInner.to_json())

# convert the object into a dict
interconnection_metro_list_metros_inner_dict = interconnection_metro_list_metros_inner_instance.to_dict()
# create an instance of InterconnectionMetroListMetrosInner from a dict
interconnection_metro_list_metros_inner_form_dict = interconnection_metro_list_metros_inner.from_dict(interconnection_metro_list_metros_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


