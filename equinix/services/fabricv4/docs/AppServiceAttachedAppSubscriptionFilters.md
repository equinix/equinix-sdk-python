# AppServiceAttachedAppSubscriptionFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[AppServiceAttachedAppSubscriptionFilter]**](AppServiceAttachedAppSubscriptionFilter.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_service_attached_app_subscription_filters import AppServiceAttachedAppSubscriptionFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceAttachedAppSubscriptionFilters from a JSON string
app_service_attached_app_subscription_filters_instance = AppServiceAttachedAppSubscriptionFilters.from_json(json)
# print the JSON string representation of the object
print(AppServiceAttachedAppSubscriptionFilters.to_json())

# convert the object into a dict
app_service_attached_app_subscription_filters_dict = app_service_attached_app_subscription_filters_instance.to_dict()
# create an instance of AppServiceAttachedAppSubscriptionFilters from a dict
app_service_attached_app_subscription_filters_from_dict = AppServiceAttachedAppSubscriptionFilters.from_dict(app_service_attached_app_subscription_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


