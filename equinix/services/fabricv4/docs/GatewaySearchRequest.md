# GatewaySearchRequest

Search gateways

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**SearchFilter**](SearchFilter.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[GatewaySortCriteria]**](GatewaySortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.gateway_search_request import GatewaySearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GatewaySearchRequest from a JSON string
gateway_search_request_instance = GatewaySearchRequest.from_json(json)
# print the JSON string representation of the object
print(GatewaySearchRequest.to_json())

# convert the object into a dict
gateway_search_request_dict = gateway_search_request_instance.to_dict()
# create an instance of GatewaySearchRequest from a dict
gateway_search_request_from_dict = GatewaySearchRequest.from_dict(gateway_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


