# AllInterconnectPackagesResponse

Interconnect Packages response <font color=\"red\"> <sup color='red'>Beta</sup></font>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[InterconnectPackage]**](InterconnectPackage.md) | List of Interconnect Packages | 

## Example

```python
from equinix.services.fabricv4.models.all_interconnect_packages_response import AllInterconnectPackagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AllInterconnectPackagesResponse from a JSON string
all_interconnect_packages_response_instance = AllInterconnectPackagesResponse.from_json(json)
# print the JSON string representation of the object
print(AllInterconnectPackagesResponse.to_json())

# convert the object into a dict
all_interconnect_packages_response_dict = all_interconnect_packages_response_instance.to_dict()
# create an instance of AllInterconnectPackagesResponse from a dict
all_interconnect_packages_response_from_dict = AllInterconnectPackagesResponse.from_dict(all_interconnect_packages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


