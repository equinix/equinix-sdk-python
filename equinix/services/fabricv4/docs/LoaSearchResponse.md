# LoaSearchResponse

List of LOAs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**sort** | [**List[LoaSortCriteria]**](LoaSortCriteria.md) |  | [optional] 
**data** | [**List[LoaResponse]**](LoaResponse.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.loa_search_response import LoaSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LoaSearchResponse from a JSON string
loa_search_response_instance = LoaSearchResponse.from_json(json)
# print the JSON string representation of the object
print(LoaSearchResponse.to_json())

# convert the object into a dict
loa_search_response_dict = loa_search_response_instance.to_dict()
# create an instance of LoaSearchResponse from a dict
loa_search_response_from_dict = LoaSearchResponse.from_dict(loa_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


