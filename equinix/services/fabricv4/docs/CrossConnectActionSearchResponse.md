# CrossConnectActionSearchResponse

List of Cross Connect Actions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**sort** | [**List[CrossConnectActionSortCriteria]**](CrossConnectActionSortCriteria.md) |  | [optional] 
**data** | [**List[CrossConnectActionResponse]**](CrossConnectActionResponse.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_action_search_response import CrossConnectActionSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectActionSearchResponse from a JSON string
cross_connect_action_search_response_instance = CrossConnectActionSearchResponse.from_json(json)
# print the JSON string representation of the object
print(CrossConnectActionSearchResponse.to_json())

# convert the object into a dict
cross_connect_action_search_response_dict = cross_connect_action_search_response_instance.to_dict()
# create an instance of CrossConnectActionSearchResponse from a dict
cross_connect_action_search_response_from_dict = CrossConnectActionSearchResponse.from_dict(cross_connect_action_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


