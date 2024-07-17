# MetroResponse

GET Metros retrieves all Equinix? Fabric? metros, as well as latency data for each location.This performance data helps network planning engineers and administrators make strategic decisions about port locations and traffic routes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[Metro]**](Metro.md) | List of Fabric Metros. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.metro_response import MetroResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MetroResponse from a JSON string
metro_response_instance = MetroResponse.from_json(json)
# print the JSON string representation of the object
print(MetroResponse.to_json())

# convert the object into a dict
metro_response_dict = metro_response_instance.to_dict()
# create an instance of MetroResponse from a dict
metro_response_form_dict = metro_response.from_dict(metro_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


