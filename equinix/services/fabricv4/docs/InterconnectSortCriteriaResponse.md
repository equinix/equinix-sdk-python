# InterconnectSortCriteriaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**InterconnectSortDirectionResponse**](InterconnectSortDirectionResponse.md) |  | [optional] [default to InterconnectSortDirectionResponse.DESC]
**var_property** | [**InterconnectSortByResponse**](InterconnectSortByResponse.md) |  | [optional] [default to InterconnectSortByResponse.CHANGE_LOG_SLASH_UPDATED_DATE_TIME]

## Example

```python
from equinix.services.fabricv4.models.interconnect_sort_criteria_response import InterconnectSortCriteriaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InterconnectSortCriteriaResponse from a JSON string
interconnect_sort_criteria_response_instance = InterconnectSortCriteriaResponse.from_json(json)
# print the JSON string representation of the object
print(InterconnectSortCriteriaResponse.to_json())

# convert the object into a dict
interconnect_sort_criteria_response_dict = interconnect_sort_criteria_response_instance.to_dict()
# create an instance of InterconnectSortCriteriaResponse from a dict
interconnect_sort_criteria_response_from_dict = InterconnectSortCriteriaResponse.from_dict(interconnect_sort_criteria_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


