# AppServiceAttachedAppSubscriptionSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**AppServiceAttachedAppSubscriptionSortDirection**](AppServiceAttachedAppSubscriptionSortDirection.md) |  | [optional] [default to AppServiceAttachedAppSubscriptionSortDirection.DESC]
**var_property** | **str** | Possible field names to use on &#39;400_InvalidSorting&#39;:   * &#x60;/uuid&#x60; - App Subscription UUID   * &#x60;/state&#x60; - App Subscription lifecycle state  | [optional] [default to '/uuid']

## Example

```python
from equinix.services.fabricv4.models.app_service_attached_app_subscription_sort_criteria import AppServiceAttachedAppSubscriptionSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceAttachedAppSubscriptionSortCriteria from a JSON string
app_service_attached_app_subscription_sort_criteria_instance = AppServiceAttachedAppSubscriptionSortCriteria.from_json(json)
# print the JSON string representation of the object
print(AppServiceAttachedAppSubscriptionSortCriteria.to_json())

# convert the object into a dict
app_service_attached_app_subscription_sort_criteria_dict = app_service_attached_app_subscription_sort_criteria_instance.to_dict()
# create an instance of AppServiceAttachedAppSubscriptionSortCriteria from a dict
app_service_attached_app_subscription_sort_criteria_from_dict = AppServiceAttachedAppSubscriptionSortCriteria.from_dict(app_service_attached_app_subscription_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


