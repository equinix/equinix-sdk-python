# ExchangeServiceSearchSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**ExchangeServiceSearchSortCriteriaDirection**](ExchangeServiceSearchSortCriteriaDirection.md) |  | [optional] [default to ExchangeServiceSearchSortCriteriaDirection.DESC]
**var_property** | [**ExchangeServiceSearchSortCriteriaProperty**](ExchangeServiceSearchSortCriteriaProperty.md) |  | [optional] [default to ExchangeServiceSearchSortCriteriaProperty.CHANGE_LOG_SLASH_UPDATED_DATE_TIME]

## Example

```python
from equinix.services.fabricv4.models.exchange_service_search_sort_criteria import ExchangeServiceSearchSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeServiceSearchSortCriteria from a JSON string
exchange_service_search_sort_criteria_instance = ExchangeServiceSearchSortCriteria.from_json(json)
# print the JSON string representation of the object
print(ExchangeServiceSearchSortCriteria.to_json())

# convert the object into a dict
exchange_service_search_sort_criteria_dict = exchange_service_search_sort_criteria_instance.to_dict()
# create an instance of ExchangeServiceSearchSortCriteria from a dict
exchange_service_search_sort_criteria_from_dict = ExchangeServiceSearchSortCriteria.from_dict(exchange_service_search_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


