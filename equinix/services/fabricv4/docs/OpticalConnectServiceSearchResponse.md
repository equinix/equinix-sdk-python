# OpticalConnectServiceSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[OpticalConnectResponse]**](OpticalConnectResponse.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.optical_connect_service_search_response import OpticalConnectServiceSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OpticalConnectServiceSearchResponse from a JSON string
optical_connect_service_search_response_instance = OpticalConnectServiceSearchResponse.from_json(json)
# print the JSON string representation of the object
print(OpticalConnectServiceSearchResponse.to_json())

# convert the object into a dict
optical_connect_service_search_response_dict = optical_connect_service_search_response_instance.to_dict()
# create an instance of OpticalConnectServiceSearchResponse from a dict
optical_connect_service_search_response_from_dict = OpticalConnectServiceSearchResponse.from_dict(optical_connect_service_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


