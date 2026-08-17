# AppDomainPostRequest

Create App Domain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AppDomainType**](AppDomainType.md) |  | [default to AppDomainType.APP_DOMAIN]
**name** | **str** | Customer-provided App Domain name | 
**description** | **str** | Customer-provided App Domain description | [optional] 
**project** | [**Project**](Project.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.app_domain_post_request import AppDomainPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppDomainPostRequest from a JSON string
app_domain_post_request_instance = AppDomainPostRequest.from_json(json)
# print the JSON string representation of the object
print(AppDomainPostRequest.to_json())

# convert the object into a dict
app_domain_post_request_dict = app_domain_post_request_instance.to_dict()
# create an instance of AppDomainPostRequest from a dict
app_domain_post_request_from_dict = AppDomainPostRequest.from_dict(app_domain_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


