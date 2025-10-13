# AllPortPackagesResponse

Port Packages response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PortPackage]**](PortPackage.md) | List of Port Packages | 

## Example

```python
from equinix.services.fabricv4.models.all_port_packages_response import AllPortPackagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AllPortPackagesResponse from a JSON string
all_port_packages_response_instance = AllPortPackagesResponse.from_json(json)
# print the JSON string representation of the object
print(AllPortPackagesResponse.to_json())

# convert the object into a dict
all_port_packages_response_dict = all_port_packages_response_instance.to_dict()
# create an instance of AllPortPackagesResponse from a dict
all_port_packages_response_from_dict = AllPortPackagesResponse.from_dict(all_port_packages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


