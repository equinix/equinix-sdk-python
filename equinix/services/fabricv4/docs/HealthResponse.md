# HealthResponse

GET Services Health

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The Canonical URL at which the resource resides. | [optional] 
**version** | **str** | Indicator of a version | [optional] 
**release** | **str** | release details. | [optional] 
**state** | **str** | status of a service | [optional] 
**api_services** | [**ApiServices**](ApiServices.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.health_response import HealthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HealthResponse from a JSON string
health_response_instance = HealthResponse.from_json(json)
# print the JSON string representation of the object
print(HealthResponse.to_json())

# convert the object into a dict
health_response_dict = health_response_instance.to_dict()
# create an instance of HealthResponse from a dict
health_response_form_dict = health_response.from_dict(health_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

