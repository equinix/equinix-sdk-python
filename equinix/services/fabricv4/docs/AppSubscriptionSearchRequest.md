# AppSubscriptionSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**AppSubscriptionFilters**](AppSubscriptionFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[AppSubscriptionSortCriteria]**](AppSubscriptionSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_subscription_search_request import AppSubscriptionSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppSubscriptionSearchRequest from a JSON string
app_subscription_search_request_instance = AppSubscriptionSearchRequest.from_json(json)
# print the JSON string representation of the object
print(AppSubscriptionSearchRequest.to_json())

# convert the object into a dict
app_subscription_search_request_dict = app_subscription_search_request_instance.to_dict()
# create an instance of AppSubscriptionSearchRequest from a dict
app_subscription_search_request_from_dict = AppSubscriptionSearchRequest.from_dict(app_subscription_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


