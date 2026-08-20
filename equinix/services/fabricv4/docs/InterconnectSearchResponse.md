# InterconnectSearchResponse

List of interconnects

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**sort** | [**List[InterconnectSortCriteriaResponse]**](InterconnectSortCriteriaResponse.md) |  | [optional] 
**data** | [**List[Interconnect]**](Interconnect.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.interconnect_search_response import InterconnectSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InterconnectSearchResponse from a JSON string
interconnect_search_response_instance = InterconnectSearchResponse.from_json(json)
# print the JSON string representation of the object
print(InterconnectSearchResponse.to_json())

# convert the object into a dict
interconnect_search_response_dict = interconnect_search_response_instance.to_dict()
# create an instance of InterconnectSearchResponse from a dict
interconnect_search_response_from_dict = InterconnectSearchResponse.from_dict(interconnect_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


