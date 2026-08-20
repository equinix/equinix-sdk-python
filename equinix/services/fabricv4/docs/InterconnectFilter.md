# InterconnectFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[InterconnectFilter]**](InterconnectFilter.md) |  | [optional] 
**var_or** | [**List[InterconnectFilter]**](InterconnectFilter.md) |  | [optional] 
**var_property** | [**InterconnectSearchFieldName**](InterconnectSearchFieldName.md) |  | [optional] 
**operator** | [**InterconnectFilterOperator**](InterconnectFilterOperator.md) |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.interconnect_filter import InterconnectFilter

# TODO update the JSON string below
json = "{}"
# create an instance of InterconnectFilter from a JSON string
interconnect_filter_instance = InterconnectFilter.from_json(json)
# print the JSON string representation of the object
print(InterconnectFilter.to_json())

# convert the object into a dict
interconnect_filter_dict = interconnect_filter_instance.to_dict()
# create an instance of InterconnectFilter from a dict
interconnect_filter_from_dict = InterconnectFilter.from_dict(interconnect_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


