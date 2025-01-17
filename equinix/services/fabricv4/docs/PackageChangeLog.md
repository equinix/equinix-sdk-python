# PackageChangeLog

Cloud Router package change log

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date_time** | **datetime** |  | [optional] 
**updated_date_time** | **datetime** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.package_change_log import PackageChangeLog

# TODO update the JSON string below
json = "{}"
# create an instance of PackageChangeLog from a JSON string
package_change_log_instance = PackageChangeLog.from_json(json)
# print the JSON string representation of the object
print(PackageChangeLog.to_json())

# convert the object into a dict
package_change_log_dict = package_change_log_instance.to_dict()
# create an instance of PackageChangeLog from a dict
package_change_log_from_dict = PackageChangeLog.from_dict(package_change_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


