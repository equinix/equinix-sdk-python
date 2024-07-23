# PrecisionTimeServicePackagesResponse

Precision Packages

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[PrecisionTimePackageResponse]**](PrecisionTimePackageResponse.md) | Data returned from the API call | [optional] 

## Example

```python
from equinix.services.fabricv4.models.precision_time_service_packages_response import PrecisionTimeServicePackagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrecisionTimeServicePackagesResponse from a JSON string
precision_time_service_packages_response_instance = PrecisionTimeServicePackagesResponse.from_json(json)
# print the JSON string representation of the object
print(PrecisionTimeServicePackagesResponse.to_json())

# convert the object into a dict
precision_time_service_packages_response_dict = precision_time_service_packages_response_instance.to_dict()
# create an instance of PrecisionTimeServicePackagesResponse from a dict
precision_time_service_packages_response_form_dict = precision_time_service_packages_response.from_dict(precision_time_service_packages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


