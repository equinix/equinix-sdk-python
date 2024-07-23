# PrecisionTimePackageRequest

EPT Package Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**code** | [**GetTimeServicesPackageByCodePackageCodeParameter**](GetTimeServicesPackageByCodePackageCodeParameter.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.precision_time_package_request import PrecisionTimePackageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrecisionTimePackageRequest from a JSON string
precision_time_package_request_instance = PrecisionTimePackageRequest.from_json(json)
# print the JSON string representation of the object
print(PrecisionTimePackageRequest.to_json())

# convert the object into a dict
precision_time_package_request_dict = precision_time_package_request_instance.to_dict()
# create an instance of PrecisionTimePackageRequest from a dict
precision_time_package_request_form_dict = precision_time_package_request.from_dict(precision_time_package_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


