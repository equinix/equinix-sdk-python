# PrecisionTimePackagePostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**code** | [**GetTimeServicesPackageByCodePackageCodeParameter**](GetTimeServicesPackageByCodePackageCodeParameter.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.precision_time_package_post_response import PrecisionTimePackagePostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrecisionTimePackagePostResponse from a JSON string
precision_time_package_post_response_instance = PrecisionTimePackagePostResponse.from_json(json)
# print the JSON string representation of the object
print(PrecisionTimePackagePostResponse.to_json())

# convert the object into a dict
precision_time_package_post_response_dict = precision_time_package_post_response_instance.to_dict()
# create an instance of PrecisionTimePackagePostResponse from a dict
precision_time_package_post_response_from_dict = PrecisionTimePackagePostResponse.from_dict(precision_time_package_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


