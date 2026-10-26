# CrossConnectProvider

Provider at the Z-Side.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the provider at the Z-Side. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_provider import CrossConnectProvider

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectProvider from a JSON string
cross_connect_provider_instance = CrossConnectProvider.from_json(json)
# print the JSON string representation of the object
print(CrossConnectProvider.to_json())

# convert the object into a dict
cross_connect_provider_dict = cross_connect_provider_instance.to_dict()
# create an instance of CrossConnectProvider from a dict
cross_connect_provider_from_dict = CrossConnectProvider.from_dict(cross_connect_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


