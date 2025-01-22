# ConnectivitySource

Physical or virtual port that houses the connection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ConnectivitySourceType**](ConnectivitySourceType.md) |  | [optional] [default to ConnectivitySourceType.COLO]

## Example

```python
from equinix.services.fabricv4.models.connectivity_source import ConnectivitySource

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectivitySource from a JSON string
connectivity_source_instance = ConnectivitySource.from_json(json)
# print the JSON string representation of the object
print(ConnectivitySource.to_json())

# convert the object into a dict
connectivity_source_dict = connectivity_source_instance.to_dict()
# create an instance of ConnectivitySource from a dict
connectivity_source_from_dict = ConnectivitySource.from_dict(connectivity_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


