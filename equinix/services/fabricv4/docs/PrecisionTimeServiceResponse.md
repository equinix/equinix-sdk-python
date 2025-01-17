# PrecisionTimeServiceResponse

Precision Time Service Response Schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Precision Time Service URI. | 
**type** | [**PrecisionTimeServiceResponseType**](PrecisionTimeServiceResponseType.md) |  | 
**name** | **str** | Precision Time Service Name. | [optional] 
**uuid** | **str** | Precision Time Service UUID. | 
**state** | [**PrecisionTimeServiceResponseState**](PrecisionTimeServiceResponseState.md) |  | 
**package** | [**PrecisionTimePackageResponse**](PrecisionTimePackageResponse.md) |  | 
**connections** | [**List[VirtualConnectionTimeServiceResponse]**](VirtualConnectionTimeServiceResponse.md) | Fabric Connections associated with Precision Time Service. | [optional] 
**ipv4** | [**Ipv4**](Ipv4.md) |  | [optional] 
**ntp_advanced_configuration** | [**List[Md5]**](Md5.md) | NTP Advanced configuration - MD5 Authentication. | [optional] 
**ptp_advanced_configuration** | [**PtpAdvanceConfiguration**](PtpAdvanceConfiguration.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | [optional] 
**order** | [**PrecisionTimeOrder**](PrecisionTimeOrder.md) |  | [optional] 
**pricing** | [**PrecisionTimePrice**](PrecisionTimePrice.md) |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.precision_time_service_response import PrecisionTimeServiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrecisionTimeServiceResponse from a JSON string
precision_time_service_response_instance = PrecisionTimeServiceResponse.from_json(json)
# print the JSON string representation of the object
print(PrecisionTimeServiceResponse.to_json())

# convert the object into a dict
precision_time_service_response_dict = precision_time_service_response_instance.to_dict()
# create an instance of PrecisionTimeServiceResponse from a dict
precision_time_service_response_from_dict = PrecisionTimeServiceResponse.from_dict(precision_time_service_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


