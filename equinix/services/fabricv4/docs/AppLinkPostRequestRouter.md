# AppLinkPostRequestRouter

Cloud Router reference for App Link

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Cloud Router UUID | 

## Example

```python
from equinix.services.fabricv4.models.app_link_post_request_router import AppLinkPostRequestRouter

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkPostRequestRouter from a JSON string
app_link_post_request_router_instance = AppLinkPostRequestRouter.from_json(json)
# print the JSON string representation of the object
print(AppLinkPostRequestRouter.to_json())

# convert the object into a dict
app_link_post_request_router_dict = app_link_post_request_router_instance.to_dict()
# create an instance of AppLinkPostRequestRouter from a dict
app_link_post_request_router_from_dict = AppLinkPostRequestRouter.from_dict(app_link_post_request_router_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


