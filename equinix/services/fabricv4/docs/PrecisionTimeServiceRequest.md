# PrecisionTimeServiceRequest

Create Precision Time Service Request Schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PrecisionTimeServiceRequestType**](PrecisionTimeServiceRequestType.md) |  | 
**name** | **str** | Precision Time Service name. | 
**package** | [**PrecisionTimePackageRequest**](PrecisionTimePackageRequest.md) |  | 
**connections** | [**List[VirtualConnectionUuid]**](VirtualConnectionUuid.md) |  | 
**ipv4** | [**Ipv4**](Ipv4.md) |  | 
**ntp_advanced_configuration** | [**List[Md5]**](Md5.md) | NTP Advanced configuration - MD5 Authentication. | [optional] 
**ptp_advanced_configuration** | [**PtpAdvanceConfiguration**](PtpAdvanceConfiguration.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**order** | [**PrecisionTimeOrder**](PrecisionTimeOrder.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.precision_time_service_request import PrecisionTimeServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrecisionTimeServiceRequest from a JSON string
precision_time_service_request_instance = PrecisionTimeServiceRequest.from_json(json)
# print the JSON string representation of the object
print(PrecisionTimeServiceRequest.to_json())

# convert the object into a dict
precision_time_service_request_dict = precision_time_service_request_instance.to_dict()
# create an instance of PrecisionTimeServiceRequest from a dict
precision_time_service_request_from_dict = PrecisionTimeServiceRequest.from_dict(precision_time_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


