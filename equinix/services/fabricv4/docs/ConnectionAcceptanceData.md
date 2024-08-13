# ConnectionAcceptanceData

Connection acceptance data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**z_side** | [**ConnectionSide**](ConnectionSide.md) |  | [optional] 
**provider_bandwidth** | **int** | Authorization key bandwidth in Mbps | [optional] [readonly] 

## Example

```python
from equinix.services.fabricv4.models.connection_acceptance_data import ConnectionAcceptanceData

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionAcceptanceData from a JSON string
connection_acceptance_data_instance = ConnectionAcceptanceData.from_json(json)
# print the JSON string representation of the object
print(ConnectionAcceptanceData.to_json())

# convert the object into a dict
connection_acceptance_data_dict = connection_acceptance_data_instance.to_dict()
# create an instance of ConnectionAcceptanceData from a dict
connection_acceptance_data_form_dict = connection_acceptance_data.from_dict(connection_acceptance_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


