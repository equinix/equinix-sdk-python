# PrecisionTimePackageResponse

EPT Service Package Information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**code** | [**GetTimeServicesPackageByCodePackageCodeParameter**](GetTimeServicesPackageByCodePackageCodeParameter.md) |  | 
**type** | [**PrecisionTimePackageResponseType**](PrecisionTimePackageResponseType.md) |  | [optional] 
**bandwidth** | **int** |  | [optional] 
**clients_per_second_max** | **int** |  | [optional] 
**redundancy_supported** | **bool** |  | [optional] 
**multi_subnet_supported** | **bool** |  | [optional] 
**accuracy_unit** | **str** |  | [optional] 
**accuracy_sla** | **int** |  | [optional] 
**accuracy_avg_min** | **int** |  | [optional] 
**accuracy_avg_max** | **int** |  | [optional] 
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
precision_time_package_response_form_dict = precision_time_package_response.from_dict(precision_time_package_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


