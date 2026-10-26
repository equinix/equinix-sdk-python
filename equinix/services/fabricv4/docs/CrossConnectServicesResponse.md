# CrossConnectServicesResponse

List of services ordered alongside the Cross Connect.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CrossConnectServiceResponse]**](CrossConnectServiceResponse.md) |  | [optional] [readonly] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_services_response import CrossConnectServicesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectServicesResponse from a JSON string
cross_connect_services_response_instance = CrossConnectServicesResponse.from_json(json)
# print the JSON string representation of the object
print(CrossConnectServicesResponse.to_json())

# convert the object into a dict
cross_connect_services_response_dict = cross_connect_services_response_instance.to_dict()
# create an instance of CrossConnectServicesResponse from a dict
cross_connect_services_response_from_dict = CrossConnectServicesResponse.from_dict(cross_connect_services_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


