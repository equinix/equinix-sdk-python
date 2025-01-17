# ValidateSubnetResponse

ValidateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_info** | [**List[ConnectionSideAdditionalInfo]**](ConnectionSideAdditionalInfo.md) | Additional information | [optional] 

## Example

```python
from equinix.services.fabricv4.models.validate_subnet_response import ValidateSubnetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateSubnetResponse from a JSON string
validate_subnet_response_instance = ValidateSubnetResponse.from_json(json)
# print the JSON string representation of the object
print(ValidateSubnetResponse.to_json())

# convert the object into a dict
validate_subnet_response_dict = validate_subnet_response_instance.to_dict()
# create an instance of ValidateSubnetResponse from a dict
validate_subnet_response_from_dict = ValidateSubnetResponse.from_dict(validate_subnet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


