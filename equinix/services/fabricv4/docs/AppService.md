# AppService

App Service object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Resource URI | [optional] [readonly] 
**type** | [**AppServiceType**](AppServiceType.md) |  | [default to AppServiceType.APP_SERVICE]
**uuid** | **str** | Equinix-assigned access point identifier | [optional] 
**name** | **str** | Customer-provided App Service name | 
**description** | **str** | Customer-provided App Service description | [optional] 
**state** | [**AppServiceState**](AppServiceState.md) |  | [optional] 
**endpoint** | **str** | Accessible endpoint through this service | [optional] 
**source_domains** | **List[str]** | List of source domains from where traffic is allowed | [optional] 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 
**change** | [**AppServiceChange**](AppServiceChange.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_service import AppService

# TODO update the JSON string below
json = "{}"
# create an instance of AppService from a JSON string
app_service_instance = AppService.from_json(json)
# print the JSON string representation of the object
print(AppService.to_json())

# convert the object into a dict
app_service_dict = app_service_instance.to_dict()
# create an instance of AppService from a dict
app_service_from_dict = AppService.from_dict(app_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


