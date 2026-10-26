# CrossConnectSearchResponse

List of Cross Connects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**sort** | [**List[CrossConnectSortCriteria]**](CrossConnectSortCriteria.md) |  | [optional] 
**data** | [**List[CrossConnectResponse]**](CrossConnectResponse.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_search_response import CrossConnectSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectSearchResponse from a JSON string
cross_connect_search_response_instance = CrossConnectSearchResponse.from_json(json)
# print the JSON string representation of the object
print(CrossConnectSearchResponse.to_json())

# convert the object into a dict
cross_connect_search_response_dict = cross_connect_search_response_instance.to_dict()
# create an instance of CrossConnectSearchResponse from a dict
cross_connect_search_response_from_dict = CrossConnectSearchResponse.from_dict(cross_connect_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


