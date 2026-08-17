# AppServiceAttachedAppSubscriptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[AppServiceAttachedAppSubscription]**](AppServiceAttachedAppSubscription.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_service_attached_app_subscriptions import AppServiceAttachedAppSubscriptions

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceAttachedAppSubscriptions from a JSON string
app_service_attached_app_subscriptions_instance = AppServiceAttachedAppSubscriptions.from_json(json)
# print the JSON string representation of the object
print(AppServiceAttachedAppSubscriptions.to_json())

# convert the object into a dict
app_service_attached_app_subscriptions_dict = app_service_attached_app_subscriptions_instance.to_dict()
# create an instance of AppServiceAttachedAppSubscriptions from a dict
app_service_attached_app_subscriptions_from_dict = AppServiceAttachedAppSubscriptions.from_dict(app_service_attached_app_subscriptions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


