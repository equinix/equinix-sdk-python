# ApiServices

Available services details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**route** | **str** | service routes | [optional] 
**status** | **str** | service status | [optional] 
**changed_date_time** | **str** | service status change date | [optional] 

## Example

```python
from equinix.services.fabricv4.models.api_services import ApiServices

# TODO update the JSON string below
json = "{}"
# create an instance of ApiServices from a JSON string
api_services_instance = ApiServices.from_json(json)
# print the JSON string representation of the object
print(ApiServices.to_json())

# convert the object into a dict
api_services_dict = api_services_instance.to_dict()
# create an instance of ApiServices from a dict
api_services_from_dict = ApiServices.from_dict(api_services_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


