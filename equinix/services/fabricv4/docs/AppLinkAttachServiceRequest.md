# AppLinkAttachServiceRequest

Attach App Service to App Link

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geo_scope** | **str** | Geo scope for the App Service | 
**destination_ip** | **str** | Target IP for forwarding API requests | 

## Example

```python
from equinix.services.fabricv4.models.app_link_attach_service_request import AppLinkAttachServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkAttachServiceRequest from a JSON string
app_link_attach_service_request_instance = AppLinkAttachServiceRequest.from_json(json)
# print the JSON string representation of the object
print(AppLinkAttachServiceRequest.to_json())

# convert the object into a dict
app_link_attach_service_request_dict = app_link_attach_service_request_instance.to_dict()
# create an instance of AppLinkAttachServiceRequest from a dict
app_link_attach_service_request_from_dict = AppLinkAttachServiceRequest.from_dict(app_link_attach_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


