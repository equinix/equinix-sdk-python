# NetworkChangeResponse

List of network changes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[NetworkChange]**](NetworkChange.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.network_change_response import NetworkChangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkChangeResponse from a JSON string
network_change_response_instance = NetworkChangeResponse.from_json(json)
# print the JSON string representation of the object
print(NetworkChangeResponse.to_json())

# convert the object into a dict
network_change_response_dict = network_change_response_instance.to_dict()
# create an instance of NetworkChangeResponse from a dict
network_change_response_form_dict = network_change_response.from_dict(network_change_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


