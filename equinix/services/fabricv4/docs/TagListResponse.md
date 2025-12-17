# TagListResponse

Equinix Fabric Tag List Response Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TagResponse]**](TagResponse.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.tag_list_response import TagListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TagListResponse from a JSON string
tag_list_response_instance = TagListResponse.from_json(json)
# print the JSON string representation of the object
print(TagListResponse.to_json())

# convert the object into a dict
tag_list_response_dict = tag_list_response_instance.to_dict()
# create an instance of TagListResponse from a dict
tag_list_response_from_dict = TagListResponse.from_dict(tag_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


