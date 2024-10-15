# GetAllStreamSubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[StreamSubscription]**](StreamSubscription.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.get_all_stream_subscription_response import GetAllStreamSubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllStreamSubscriptionResponse from a JSON string
get_all_stream_subscription_response_instance = GetAllStreamSubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllStreamSubscriptionResponse.to_json())

# convert the object into a dict
get_all_stream_subscription_response_dict = get_all_stream_subscription_response_instance.to_dict()
# create an instance of GetAllStreamSubscriptionResponse from a dict
get_all_stream_subscription_response_form_dict = get_all_stream_subscription_response.from_dict(get_all_stream_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


