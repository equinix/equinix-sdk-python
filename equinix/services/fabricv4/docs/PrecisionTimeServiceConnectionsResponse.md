# PrecisionTimeServiceConnectionsResponse

EPT service instance's L2 connections

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[ConnectionLink]**](ConnectionLink.md) | Data returned from the API call | [optional] 

## Example

```python
from equinix.services.fabricv4.models.precision_time_service_connections_response import PrecisionTimeServiceConnectionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrecisionTimeServiceConnectionsResponse from a JSON string
precision_time_service_connections_response_instance = PrecisionTimeServiceConnectionsResponse.from_json(json)
# print the JSON string representation of the object
print(PrecisionTimeServiceConnectionsResponse.to_json())

# convert the object into a dict
precision_time_service_connections_response_dict = precision_time_service_connections_response_instance.to_dict()
# create an instance of PrecisionTimeServiceConnectionsResponse from a dict
precision_time_service_connections_response_from_dict = PrecisionTimeServiceConnectionsResponse.from_dict(precision_time_service_connections_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


