# ServiceMetros

Service Profile Metros

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ServiceMetro]**](ServiceMetro.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_metros import ServiceMetros

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceMetros from a JSON string
service_metros_instance = ServiceMetros.from_json(json)
# print the JSON string representation of the object
print(ServiceMetros.to_json())

# convert the object into a dict
service_metros_dict = service_metros_instance.to_dict()
# create an instance of ServiceMetros from a dict
service_metros_form_dict = service_metros.from_dict(service_metros_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


