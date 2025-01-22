# PackageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[CloudRouterPackage]**](CloudRouterPackage.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.package_response import PackageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PackageResponse from a JSON string
package_response_instance = PackageResponse.from_json(json)
# print the JSON string representation of the object
print(PackageResponse.to_json())

# convert the object into a dict
package_response_dict = package_response_instance.to_dict()
# create an instance of PackageResponse from a dict
package_response_from_dict = PackageResponse.from_dict(package_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


