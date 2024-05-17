# IPAvailabilitiesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **List[str]** |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.ip_availabilities_list import IPAvailabilitiesList

# TODO update the JSON string below
json = "{}"
# create an instance of IPAvailabilitiesList from a JSON string
ip_availabilities_list_instance = IPAvailabilitiesList.from_json(json)
# print the JSON string representation of the object
print(IPAvailabilitiesList.to_json())

# convert the object into a dict
ip_availabilities_list_dict = ip_availabilities_list_instance.to_dict()
# create an instance of IPAvailabilitiesList from a dict
ip_availabilities_list_form_dict = ip_availabilities_list.from_dict(ip_availabilities_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


