# AppSubscriptionSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**AppSubscriptionSortDirection**](AppSubscriptionSortDirection.md) |  | [optional] [default to AppSubscriptionSortDirection.DESC]
**var_property** | **str** | Possible field names to use on &#39;400_InvalidSorting&#39;:   * &#x60;/uuid&#x60; - App Subscription uuid   * &#x60;/state&#x60; - App Subscription status   * &#x60;/changeLog/createdDateTime&#x60; - Date and time when change flow starts   * &#x60;/changeLog/updatedDateTime&#x60; - Date and time when change object is updated  | [optional] [default to '/changeLog/updatedDateTime']

## Example

```python
from equinix.services.fabricv4.models.app_subscription_sort_criteria import AppSubscriptionSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of AppSubscriptionSortCriteria from a JSON string
app_subscription_sort_criteria_instance = AppSubscriptionSortCriteria.from_json(json)
# print the JSON string representation of the object
print(AppSubscriptionSortCriteria.to_json())

# convert the object into a dict
app_subscription_sort_criteria_dict = app_subscription_sort_criteria_instance.to_dict()
# create an instance of AppSubscriptionSortCriteria from a dict
app_subscription_sort_criteria_from_dict = AppSubscriptionSortCriteria.from_dict(app_subscription_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


