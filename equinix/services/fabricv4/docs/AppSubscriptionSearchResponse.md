# AppSubscriptionSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[AppSubscription]**](AppSubscription.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_subscription_search_response import AppSubscriptionSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppSubscriptionSearchResponse from a JSON string
app_subscription_search_response_instance = AppSubscriptionSearchResponse.from_json(json)
# print the JSON string representation of the object
print(AppSubscriptionSearchResponse.to_json())

# convert the object into a dict
app_subscription_search_response_dict = app_subscription_search_response_instance.to_dict()
# create an instance of AppSubscriptionSearchResponse from a dict
app_subscription_search_response_from_dict = AppSubscriptionSearchResponse.from_dict(app_subscription_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


