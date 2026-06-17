# IpBlocksSearchRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**filter** | [**IpBlockFilter**](IpBlockFilter.md) |  | [optional] 
**sort** | [**List[SearchSortItem]**](SearchSortItem.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.ip_blocks_search_request_body import IpBlocksSearchRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of IpBlocksSearchRequestBody from a JSON string
ip_blocks_search_request_body_instance = IpBlocksSearchRequestBody.from_json(json)
# print the JSON string representation of the object
print(IpBlocksSearchRequestBody.to_json())

# convert the object into a dict
ip_blocks_search_request_body_dict = ip_blocks_search_request_body_instance.to_dict()
# create an instance of IpBlocksSearchRequestBody from a dict
ip_blocks_search_request_body_from_dict = IpBlocksSearchRequestBody.from_dict(ip_blocks_search_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


