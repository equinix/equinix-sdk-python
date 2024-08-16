# SubscriptionTrial

Trial

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**expiry_date_time** | **datetime** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.subscription_trial import SubscriptionTrial

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionTrial from a JSON string
subscription_trial_instance = SubscriptionTrial.from_json(json)
# print the JSON string representation of the object
print(SubscriptionTrial.to_json())

# convert the object into a dict
subscription_trial_dict = subscription_trial_instance.to_dict()
# create an instance of SubscriptionTrial from a dict
subscription_trial_form_dict = subscription_trial.from_dict(subscription_trial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


