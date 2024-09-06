# ConnectionResponse

ValidateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_info** | [**List[ConnectionSideAdditionalInfo]**](ConnectionSideAdditionalInfo.md) | Additional information | [optional] 
**data** | [**List[Connection]**](Connection.md) | Connection response data | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connection_response import ConnectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionResponse from a JSON string
connection_response_instance = ConnectionResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectionResponse.to_json())

# convert the object into a dict
connection_response_dict = connection_response_instance.to_dict()
# create an instance of ConnectionResponse from a dict
connection_response_from_dict = ConnectionResponse.from_dict(connection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


