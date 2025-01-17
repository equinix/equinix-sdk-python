# GetAllStreamResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[Stream]**](Stream.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.get_all_stream_response import GetAllStreamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllStreamResponse from a JSON string
get_all_stream_response_instance = GetAllStreamResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllStreamResponse.to_json())

# convert the object into a dict
get_all_stream_response_dict = get_all_stream_response_instance.to_dict()
# create an instance of GetAllStreamResponse from a dict
get_all_stream_response_from_dict = GetAllStreamResponse.from_dict(get_all_stream_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


