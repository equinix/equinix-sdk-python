# ValidateConnectionResponse

Validate Connection specification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Equinix-assigned connection identifier | [optional] 
**bandwidth** | **int** | Connection bandwidth in Mbps | [optional] 
**redundancy** | [**ConnectionRedundancy**](ConnectionRedundancy.md) |  | [optional] 
**a_side** | [**ConnectionSide**](ConnectionSide.md) |  | [optional] 
**z_side** | [**ConnectionSide**](ConnectionSide.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.validate_connection_response import ValidateConnectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateConnectionResponse from a JSON string
validate_connection_response_instance = ValidateConnectionResponse.from_json(json)
# print the JSON string representation of the object
print(ValidateConnectionResponse.to_json())

# convert the object into a dict
validate_connection_response_dict = validate_connection_response_instance.to_dict()
# create an instance of ValidateConnectionResponse from a dict
validate_connection_response_form_dict = validate_connection_response.from_dict(validate_connection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


