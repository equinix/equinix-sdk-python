# StreamSubscriptionOperationAdditionalInfo

External error information from subscription sink

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Additional attribute for error information | [optional] 
**status_code** | **str** | HTTP error status code response from sink type if error occurred | [optional] 
**reason** | **str** | HTTP error message response from sink type if error occurred | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_subscription_operation_additional_info import StreamSubscriptionOperationAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StreamSubscriptionOperationAdditionalInfo from a JSON string
stream_subscription_operation_additional_info_instance = StreamSubscriptionOperationAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(StreamSubscriptionOperationAdditionalInfo.to_json())

# convert the object into a dict
stream_subscription_operation_additional_info_dict = stream_subscription_operation_additional_info_instance.to_dict()
# create an instance of StreamSubscriptionOperationAdditionalInfo from a dict
stream_subscription_operation_additional_info_from_dict = StreamSubscriptionOperationAdditionalInfo.from_dict(stream_subscription_operation_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


