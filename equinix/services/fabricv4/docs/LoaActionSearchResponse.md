# LoaActionSearchResponse

List of LOA Actions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**sort** | [**List[LoaActionSortCriteria]**](LoaActionSortCriteria.md) |  | [optional] 
**data** | [**List[LoaActionResponse]**](LoaActionResponse.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.loa_action_search_response import LoaActionSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LoaActionSearchResponse from a JSON string
loa_action_search_response_instance = LoaActionSearchResponse.from_json(json)
# print the JSON string representation of the object
print(LoaActionSearchResponse.to_json())

# convert the object into a dict
loa_action_search_response_dict = loa_action_search_response_instance.to_dict()
# create an instance of LoaActionSearchResponse from a dict
loa_action_search_response_from_dict = LoaActionSearchResponse.from_dict(loa_action_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


