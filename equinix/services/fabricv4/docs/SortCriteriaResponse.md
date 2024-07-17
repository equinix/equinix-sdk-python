# SortCriteriaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**SortDirection**](SortDirection.md) |  | [optional] 
**var_property** | [**SortBy**](SortBy.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.sort_criteria_response import SortCriteriaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SortCriteriaResponse from a JSON string
sort_criteria_response_instance = SortCriteriaResponse.from_json(json)
# print the JSON string representation of the object
print(SortCriteriaResponse.to_json())

# convert the object into a dict
sort_criteria_response_dict = sort_criteria_response_instance.to_dict()
# create an instance of SortCriteriaResponse from a dict
sort_criteria_response_form_dict = sort_criteria_response.from_dict(sort_criteria_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


