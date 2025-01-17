# PrecisionTimePackageResponse

EPT Service Package Information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**type** | [**PrecisionTimePackageResponseType**](PrecisionTimePackageResponseType.md) |  | 
**code** | [**GetTimeServicesPackageByCodePackageCodeParameter**](GetTimeServicesPackageByCodePackageCodeParameter.md) |  | 
**bandwidth** | **int** | Connection bandwidth in Mbps. | 
**clients_per_second_max** | **int** | Max. number of clients that can be synchronized per second at a packet rate of 1 per second. | [optional] 
**redundancy_supported** | **bool** | Is Redundant virtual connection supported for the package code. | [optional] 
**multi_subnet_supported** | **bool** | Is Multiple subnet supported for the package code. | [optional] 
**accuracy_sla_unit** | **str** | Accuracy SLA unit. | [optional] 
**accuracy_sla** | **int** | Accuracy SLA for the package code, -1 value denotes the accuracySla is not published. | [optional] 
**accuracy_sla_min** | **int** | Typical minimum Accuracy for the package code. | [optional] 
**accuracy_sla_max** | **int** | Typical maximum Accuracy for the package code. | [optional] 
**changelog** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.precision_time_package_response import PrecisionTimePackageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrecisionTimePackageResponse from a JSON string
precision_time_package_response_instance = PrecisionTimePackageResponse.from_json(json)
# print the JSON string representation of the object
print(PrecisionTimePackageResponse.to_json())

# convert the object into a dict
precision_time_package_response_dict = precision_time_package_response_instance.to_dict()
# create an instance of PrecisionTimePackageResponse from a dict
precision_time_package_response_from_dict = PrecisionTimePackageResponse.from_dict(precision_time_package_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


