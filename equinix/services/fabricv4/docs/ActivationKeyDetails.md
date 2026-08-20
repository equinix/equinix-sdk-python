# ActivationKeyDetails

Activation Key Details <sup color='red'>Beta</sup></font>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Provider Encoded activation key | [optional] 
**provider_id** | **str** | AWS Connection identifier | [optional] 
**account_id** | **str** | Account identifier | [optional] 
**bandwidth** | **int** | Bandwidth in Mbps | [optional] 
**region** | **str** | Cloud provider region identifier | [optional] 

## Example

```python
from equinix.services.fabricv4.models.activation_key_details import ActivationKeyDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ActivationKeyDetails from a JSON string
activation_key_details_instance = ActivationKeyDetails.from_json(json)
# print the JSON string representation of the object
print(ActivationKeyDetails.to_json())

# convert the object into a dict
activation_key_details_dict = activation_key_details_instance.to_dict()
# create an instance of ActivationKeyDetails from a dict
activation_key_details_from_dict = ActivationKeyDetails.from_dict(activation_key_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


