# PrecisionTimeServiceRequest

EPT service instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PrecisionTimeServiceRequestType**](PrecisionTimeServiceRequestType.md) |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**package** | [**PrecisionTimePackageRequest**](PrecisionTimePackageRequest.md) |  | 
**connections** | [**List[FabricConnectionUuid]**](FabricConnectionUuid.md) |  | 
**ipv4** | [**Ipv4**](Ipv4.md) |  | 
**advance_configuration** | [**AdvanceConfiguration**](AdvanceConfiguration.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 

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
precision_time_service_request_form_dict = precision_time_service_request.from_dict(precision_time_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


