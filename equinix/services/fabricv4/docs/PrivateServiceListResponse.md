# PrivateServiceListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PrivateService]**](PrivateService.md) | List of private services | [optional] 

## Example

```python
from equinix.services.fabricv4.models.private_service_list_response import PrivateServiceListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateServiceListResponse from a JSON string
private_service_list_response_instance = PrivateServiceListResponse.from_json(json)
# print the JSON string representation of the object
print(PrivateServiceListResponse.to_json())

# convert the object into a dict
private_service_list_response_dict = private_service_list_response_instance.to_dict()
# create an instance of PrivateServiceListResponse from a dict
private_service_list_response_from_dict = PrivateServiceListResponse.from_dict(private_service_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


