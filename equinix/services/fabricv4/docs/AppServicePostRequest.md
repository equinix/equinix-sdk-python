# AppServicePostRequest

Create App Service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AppServiceType**](AppServiceType.md) |  | [default to AppServiceType.APP_SERVICE]
**name** | **str** | Customer-provided App Service name | 
**description** | **str** | Customer-provided App Service description | [optional] 
**endpoint** | **str** | Accessible endpoint through this service | 
**source_domains** | **List[str]** | List of source domains from where traffic is allowed | [optional] 
**project** | [**Project**](Project.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.app_service_post_request import AppServicePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppServicePostRequest from a JSON string
app_service_post_request_instance = AppServicePostRequest.from_json(json)
# print the JSON string representation of the object
print(AppServicePostRequest.to_json())

# convert the object into a dict
app_service_post_request_dict = app_service_post_request_instance.to_dict()
# create an instance of AppServicePostRequest from a dict
app_service_post_request_from_dict = AppServicePostRequest.from_dict(app_service_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


