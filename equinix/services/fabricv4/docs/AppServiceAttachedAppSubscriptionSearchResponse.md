# AppServiceAttachedAppSubscriptionSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[AppServiceAttachedAppSubscription]**](AppServiceAttachedAppSubscription.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_service_attached_app_subscription_search_response import AppServiceAttachedAppSubscriptionSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceAttachedAppSubscriptionSearchResponse from a JSON string
app_service_attached_app_subscription_search_response_instance = AppServiceAttachedAppSubscriptionSearchResponse.from_json(json)
# print the JSON string representation of the object
print(AppServiceAttachedAppSubscriptionSearchResponse.to_json())

# convert the object into a dict
app_service_attached_app_subscription_search_response_dict = app_service_attached_app_subscription_search_response_instance.to_dict()
# create an instance of AppServiceAttachedAppSubscriptionSearchResponse from a dict
app_service_attached_app_subscription_search_response_from_dict = AppServiceAttachedAppSubscriptionSearchResponse.from_dict(app_service_attached_app_subscription_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


