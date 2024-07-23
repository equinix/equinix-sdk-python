# PrecisionTimeServiceCreateResponse

EPT service instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PrecisionTimeServiceCreateResponseType**](PrecisionTimeServiceCreateResponseType.md) |  | 
**href** | **str** |  | 
**uuid** | **str** | uuid of the ept service | 
**name** | **str** | name of the ept service | [optional] 
**description** | **str** |  | [optional] 
**state** | [**PrecisionTimeServiceCreateResponseState**](PrecisionTimeServiceCreateResponseState.md) |  | 
**package** | [**PrecisionTimePackageResponse**](PrecisionTimePackageResponse.md) |  | 
**connections** | [**List[FabricConnectionUuid]**](FabricConnectionUuid.md) | fabric l2 connections used for the ept service | [optional] 
**ipv4** | [**Ipv4**](Ipv4.md) |  | 
**account** | [**Account**](Account.md) |  | [optional] 
**advance_configuration** | [**AdvanceConfiguration**](AdvanceConfiguration.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.precision_time_service_create_response import PrecisionTimeServiceCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrecisionTimeServiceCreateResponse from a JSON string
precision_time_service_create_response_instance = PrecisionTimeServiceCreateResponse.from_json(json)
# print the JSON string representation of the object
print(PrecisionTimeServiceCreateResponse.to_json())

# convert the object into a dict
precision_time_service_create_response_dict = precision_time_service_create_response_instance.to_dict()
# create an instance of PrecisionTimeServiceCreateResponse from a dict
precision_time_service_create_response_form_dict = precision_time_service_create_response.from_dict(precision_time_service_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


