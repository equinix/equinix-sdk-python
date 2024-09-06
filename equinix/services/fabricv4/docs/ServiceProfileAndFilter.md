# ServiceProfileAndFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[ServiceProfileSimpleExpression]**](ServiceProfileSimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_profile_and_filter import ServiceProfileAndFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileAndFilter from a JSON string
service_profile_and_filter_instance = ServiceProfileAndFilter.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileAndFilter.to_json())

# convert the object into a dict
service_profile_and_filter_dict = service_profile_and_filter_instance.to_dict()
# create an instance of ServiceProfileAndFilter from a dict
service_profile_and_filter_from_dict = ServiceProfileAndFilter.from_dict(service_profile_and_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


