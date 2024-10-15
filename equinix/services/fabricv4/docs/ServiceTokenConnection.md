# ServiceTokenConnection

Service Token Connection Type Information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ServiceTokenConnectionType**](ServiceTokenConnectionType.md) |  | 
**href** | **str** | An absolute URL that is the subject of the link&#39;s context. | [optional] [readonly] 
**uuid** | **str** | Equinix-assigned connection identifier | [optional] 
**allow_remote_connection** | **bool** | Authorization to connect remotely | [optional] [default to False]
**allow_custom_bandwidth** | **bool** | Allow custom bandwidth value | [optional] [default to False]
**bandwidth_limit** | **int** | Connection bandwidth limit in Mbps | [optional] 
**supported_bandwidths** | **List[int]** | List of permitted bandwidths. | [optional] 
**a_side** | [**ServiceTokenSide**](ServiceTokenSide.md) |  | [optional] 
**z_side** | [**ServiceTokenSide**](ServiceTokenSide.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_token_connection import ServiceTokenConnection

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTokenConnection from a JSON string
service_token_connection_instance = ServiceTokenConnection.from_json(json)
# print the JSON string representation of the object
print(ServiceTokenConnection.to_json())

# convert the object into a dict
service_token_connection_dict = service_token_connection_instance.to_dict()
# create an instance of ServiceTokenConnection from a dict
service_token_connection_form_dict = service_token_connection.from_dict(service_token_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


