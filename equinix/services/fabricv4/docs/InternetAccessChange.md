# InternetAccessChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | URI of the change object | 

## Example

```python
from equinix.services.fabricv4.models.internet_access_change import InternetAccessChange

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessChange from a JSON string
internet_access_change_instance = InternetAccessChange.from_json(json)
# print the JSON string representation of the object
print(InternetAccessChange.to_json())

# convert the object into a dict
internet_access_change_dict = internet_access_change_instance.to_dict()
# create an instance of InternetAccessChange from a dict
internet_access_change_from_dict = InternetAccessChange.from_dict(internet_access_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


