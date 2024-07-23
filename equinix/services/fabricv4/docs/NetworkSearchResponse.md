# NetworkSearchResponse

List of networks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**sort** | [**List[NetworkSortCriteriaResponse]**](NetworkSortCriteriaResponse.md) |  | [optional] 
**data** | [**List[Network]**](Network.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.network_search_response import NetworkSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkSearchResponse from a JSON string
network_search_response_instance = NetworkSearchResponse.from_json(json)
# print the JSON string representation of the object
print(NetworkSearchResponse.to_json())

# convert the object into a dict
network_search_response_dict = network_search_response_instance.to_dict()
# create an instance of NetworkSearchResponse from a dict
network_search_response_form_dict = network_search_response.from_dict(network_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


