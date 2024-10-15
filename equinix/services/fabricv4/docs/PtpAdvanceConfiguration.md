# PtpAdvanceConfiguration

PTP Advanced Configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_scale** | [**PtpAdvanceConfigurationTimeScale**](PtpAdvanceConfigurationTimeScale.md) |  | [optional] 
**domain** | **int** | The PTP domain value. | [optional] 
**priority1** | **int** | The priority1 value determines the best primary clock, Lower value indicates higher priority. | [optional] 
**priority2** | **int** | The priority2 value differentiates and prioritizes the primary clock to avoid confusion when priority1-value is the same for different primary clocks in a network. | [optional] 
**log_announce_interval** | [**PtpAdvanceConfigurationLogAnnounceInterval**](PtpAdvanceConfigurationLogAnnounceInterval.md) |  | [optional] 
**log_sync_interval** | [**PtpAdvanceConfigurationLogSyncInterval**](PtpAdvanceConfigurationLogSyncInterval.md) |  | [optional] 
**log_delay_req_interval** | [**PtpAdvanceConfigurationLogDelayReqInterval**](PtpAdvanceConfigurationLogDelayReqInterval.md) |  | [optional] 
**transport_mode** | [**PtpAdvanceConfigurationTransportMode**](PtpAdvanceConfigurationTransportMode.md) |  | [optional] 
**grant_time** | **int** | Unicast Grant Time in seconds. For Multicast and Hybrid transport modes, grant time defaults to 300 seconds. For Unicast mode, grant time can be between 30 to 7200. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.ptp_advance_configuration import PtpAdvanceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of PtpAdvanceConfiguration from a JSON string
ptp_advance_configuration_instance = PtpAdvanceConfiguration.from_json(json)
# print the JSON string representation of the object
print(PtpAdvanceConfiguration.to_json())

# convert the object into a dict
ptp_advance_configuration_dict = ptp_advance_configuration_instance.to_dict()
# create an instance of PtpAdvanceConfiguration from a dict
ptp_advance_configuration_form_dict = ptp_advance_configuration.from_dict(ptp_advance_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


