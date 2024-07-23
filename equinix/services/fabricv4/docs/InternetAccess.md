# InternetAccess

Internet Access Details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Internet Access Service Identifier | [optional] 

## Example

```python
from equinix.services.fabricv4.models.internet_access import InternetAccess

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccess from a JSON string
internet_access_instance = InternetAccess.from_json(json)
# print the JSON string representation of the object
print(InternetAccess.to_json())

# convert the object into a dict
internet_access_dict = internet_access_instance.to_dict()
# create an instance of InternetAccess from a dict
internet_access_form_dict = internet_access.from_dict(internet_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


