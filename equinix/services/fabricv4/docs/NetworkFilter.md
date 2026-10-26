# NetworkFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[NetworkFilter]**](NetworkFilter.md) |  | [optional] 
**var_or** | [**List[NetworkFilter]**](NetworkFilter.md) |  | [optional] 
**var_property** | [**NetworkSearchFieldName**](NetworkSearchFieldName.md) |  | [optional] 
**operator** | [**NetworkFilterOperator**](NetworkFilterOperator.md) |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.network_filter import NetworkFilter

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkFilter from a JSON string
network_filter_instance = NetworkFilter.from_json(json)
# print the JSON string representation of the object
print(NetworkFilter.to_json())

# convert the object into a dict
network_filter_dict = network_filter_instance.to_dict()
# create an instance of NetworkFilter from a dict
network_filter_from_dict = NetworkFilter.from_dict(network_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


