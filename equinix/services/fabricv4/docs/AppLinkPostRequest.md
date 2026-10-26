# AppLinkPostRequest

Create App Link

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AppLinkType**](AppLinkType.md) |  | [default to AppLinkType.APP_LINK]
**name** | **str** | Customer-provided App Link name | 
**description** | **str** | Customer-provided App Link description | [optional] 
**router** | [**AppLinkPostRequestRouter**](AppLinkPostRequestRouter.md) |  | 
**ipv4_subnet** | **str** | Customer-provided IP subnet for AppLink setup (/29 or larger subnet) | 
**bandwidth** | **int** | App Link aggregated data transfer capacity in Mbps | 
**project** | [**Project**](Project.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.app_link_post_request import AppLinkPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkPostRequest from a JSON string
app_link_post_request_instance = AppLinkPostRequest.from_json(json)
# print the JSON string representation of the object
print(AppLinkPostRequest.to_json())

# convert the object into a dict
app_link_post_request_dict = app_link_post_request_instance.to_dict()
# create an instance of AppLinkPostRequest from a dict
app_link_post_request_from_dict = AppLinkPostRequest.from_dict(app_link_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


