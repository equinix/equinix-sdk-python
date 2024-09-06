# ServiceSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[PrecisionTimeServiceResponse]**](PrecisionTimeServiceResponse.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_search_response import ServiceSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSearchResponse from a JSON string
service_search_response_instance = ServiceSearchResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceSearchResponse.to_json())

# convert the object into a dict
service_search_response_dict = service_search_response_instance.to_dict()
# create an instance of ServiceSearchResponse from a dict
service_search_response_from_dict = ServiceSearchResponse.from_dict(service_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


