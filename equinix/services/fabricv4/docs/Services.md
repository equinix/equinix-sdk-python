# Services

Arrays of objects containing type of services supported in the specified metros

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of Service | [optional] 

## Example

```python
from equinix.services.fabricv4.models.services import Services

# TODO update the JSON string below
json = "{}"
# create an instance of Services from a JSON string
services_instance = Services.from_json(json)
# print the JSON string representation of the object
print(Services.to_json())

# convert the object into a dict
services_dict = services_instance.to_dict()
# create an instance of Services from a dict
services_from_dict = Services.from_dict(services_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


