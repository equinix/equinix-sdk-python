# PtpAdvanceConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_scale** | [**PtpAdvanceConfigurationTimeScale**](PtpAdvanceConfigurationTimeScale.md) |  | [optional] 
**domain** | **int** |  | [optional] 
**priority1** | **int** |  | [optional] 
**priority2** | **int** |  | [optional] 
**log_announce_interval** | **int** | The mean time interval between Announce messages. A shorter interval makes ptp4l react faster to the changes in the master-slave hierarchy. The interval should be the same in the whole domain. It&#39;s specified as a power of two in seconds. The default is 1 (2 seconds). | [optional] 
**log_sync_interval** | **int** | The mean time interval between Sync messages. A shorter interval may improve accuracy of the local clock. It&#39;s specified as a power of two in seconds. The default is 0 (1 second). | [optional] 
**log_delay_req_interval** | **int** |  | [optional] 
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
ptp_advance_configuration_from_dict = PtpAdvanceConfiguration.from_dict(ptp_advance_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


