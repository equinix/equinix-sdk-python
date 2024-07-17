# NetworkSortCriteriaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**NetworkSortDirectionResponse**](NetworkSortDirectionResponse.md) |  | [optional] 
**var_property** | [**NetworkSortByResponse**](NetworkSortByResponse.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.network_sort_criteria_response import NetworkSortCriteriaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkSortCriteriaResponse from a JSON string
network_sort_criteria_response_instance = NetworkSortCriteriaResponse.from_json(json)
# print the JSON string representation of the object
print(NetworkSortCriteriaResponse.to_json())

# convert the object into a dict
network_sort_criteria_response_dict = network_sort_criteria_response_instance.to_dict()
# create an instance of NetworkSortCriteriaResponse from a dict
network_sort_criteria_response_form_dict = network_sort_criteria_response.from_dict(network_sort_criteria_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


