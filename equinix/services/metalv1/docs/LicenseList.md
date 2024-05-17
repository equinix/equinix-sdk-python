# LicenseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**licenses** | [**List[License]**](License.md) |  | [optional] 

## Example

```python
from equinix_metal.models.license_list import LicenseList

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseList from a JSON string
license_list_instance = LicenseList.from_json(json)
# print the JSON string representation of the object
print(LicenseList.to_json())

# convert the object into a dict
license_list_dict = license_list_instance.to_dict()
# create an instance of LicenseList from a dict
license_list_form_dict = license_list.from_dict(license_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


