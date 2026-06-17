# InternetAccessSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**filter** | [**SearchExpression**](SearchExpression.md) |  | [optional] 
**sort** | [**List[SearchSortItem]**](SearchSortItem.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.internet_access_search_request import InternetAccessSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessSearchRequest from a JSON string
internet_access_search_request_instance = InternetAccessSearchRequest.from_json(json)
# print the JSON string representation of the object
print(InternetAccessSearchRequest.to_json())

# convert the object into a dict
internet_access_search_request_dict = internet_access_search_request_instance.to_dict()
# create an instance of InternetAccessSearchRequest from a dict
internet_access_search_request_from_dict = InternetAccessSearchRequest.from_dict(internet_access_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


