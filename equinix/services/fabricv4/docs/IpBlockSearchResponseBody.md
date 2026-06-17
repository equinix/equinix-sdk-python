# IpBlockSearchResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**sort** | [**List[SearchSortItem]**](SearchSortItem.md) |  | [optional] 
**data** | [**List[IpBlock]**](IpBlock.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.ip_block_search_response_body import IpBlockSearchResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of IpBlockSearchResponseBody from a JSON string
ip_block_search_response_body_instance = IpBlockSearchResponseBody.from_json(json)
# print the JSON string representation of the object
print(IpBlockSearchResponseBody.to_json())

# convert the object into a dict
ip_block_search_response_body_dict = ip_block_search_response_body_instance.to_dict()
# create an instance of IpBlockSearchResponseBody from a dict
ip_block_search_response_body_from_dict = IpBlockSearchResponseBody.from_dict(ip_block_search_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


