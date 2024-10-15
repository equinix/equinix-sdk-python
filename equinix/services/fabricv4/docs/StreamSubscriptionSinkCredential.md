# StreamSubscriptionSinkCredential

Stream subscription sink credentials

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**StreamSubscriptionSinkCredentialType**](StreamSubscriptionSinkCredentialType.md) |  | [optional] 
**access_token** | **str** | passed as Authorization header value | [optional] 
**integration_key** | **str** | passed as Authorization header value | [optional] 
**api_key** | **str** | passed as Authorization header value | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_subscription_sink_credential import StreamSubscriptionSinkCredential

# TODO update the JSON string below
json = "{}"
# create an instance of StreamSubscriptionSinkCredential from a JSON string
stream_subscription_sink_credential_instance = StreamSubscriptionSinkCredential.from_json(json)
# print the JSON string representation of the object
print(StreamSubscriptionSinkCredential.to_json())

# convert the object into a dict
stream_subscription_sink_credential_dict = stream_subscription_sink_credential_instance.to_dict()
# create an instance of StreamSubscriptionSinkCredential from a dict
stream_subscription_sink_credential_form_dict = stream_subscription_sink_credential.from_dict(stream_subscription_sink_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


