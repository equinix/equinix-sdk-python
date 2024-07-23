# AdvanceConfiguration

Advance Configuration for NTP/PTP

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ntp** | [**List[Md5]**](Md5.md) |  | [optional] 
**ptp** | [**PtpAdvanceConfiguration**](PtpAdvanceConfiguration.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.advance_configuration import AdvanceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AdvanceConfiguration from a JSON string
advance_configuration_instance = AdvanceConfiguration.from_json(json)
# print the JSON string representation of the object
print(AdvanceConfiguration.to_json())

# convert the object into a dict
advance_configuration_dict = advance_configuration_instance.to_dict()
# create an instance of AdvanceConfiguration from a dict
advance_configuration_form_dict = advance_configuration.from_dict(advance_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


