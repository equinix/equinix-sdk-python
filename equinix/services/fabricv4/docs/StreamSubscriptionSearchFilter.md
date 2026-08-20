# StreamSubscriptionSearchFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Possible field names to use on filters:  * &#x60;/uuid&#x60; - Subscription uuid  * &#x60;/streamUuid&#x60; - Stream uuid the subscription belongs to  * &#x60;/state&#x60; - Subscription state (&#x60;DEPROVISIONED&#x60; returned only when explicitly requested)  * &#x60;/name&#x60; - Subscription name  * &#x60;/project/projectId&#x60; - Subscription project id  * &#x60;/description&#x60; - Subscription description  * &#x60;/changeLog/createdDateTime&#x60; - Subscription created date time  * &#x60;/changeLog/updatedDateTime&#x60; - Subscription updated date time  | [optional] 
**operator** | **str** | Possible operators to use on filters:  * &#x60;&#x3D;&#x60; - equal  * &#x60;!&#x3D;&#x60; - not equal  * &#x60;&gt;&#x60; - greater than  * &#x60;&gt;&#x3D;&#x60; - greater than or equal to  * &#x60;&lt;&#x60; - less than  * &#x60;&lt;&#x3D;&#x60; - less than or equal to  * &#x60;BETWEEN&#x60; - between  * &#x60;NOT BETWEEN&#x60; - not between  * &#x60;LIKE&#x60; - like  * &#x60;ILIKE&#x60; - like case-insensitive  * &#x60;IN&#x60; - in  * &#x60;NOT IN&#x60; - not in  | [optional] 
**values** | **List[str]** |  | [optional] 
**var_or** | [**List[StreamSubscriptionSearchSimpleExpression]**](StreamSubscriptionSearchSimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_subscription_search_filter import StreamSubscriptionSearchFilter

# TODO update the JSON string below
json = "{}"
# create an instance of StreamSubscriptionSearchFilter from a JSON string
stream_subscription_search_filter_instance = StreamSubscriptionSearchFilter.from_json(json)
# print the JSON string representation of the object
print(StreamSubscriptionSearchFilter.to_json())

# convert the object into a dict
stream_subscription_search_filter_dict = stream_subscription_search_filter_instance.to_dict()
# create an instance of StreamSubscriptionSearchFilter from a dict
stream_subscription_search_filter_from_dict = StreamSubscriptionSearchFilter.from_dict(stream_subscription_search_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


