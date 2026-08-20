# ServiceProfileLastMileApiIntegration

Last-mile API integration details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_validation_enabled** | **bool** | Whether site validation is enabled for the last-mile provider. | [optional] 
**data_center_location_enabled** | **bool** | Whether data center location is enabled for the last-mile provider. | [optional] 
**product_offering_enabled** | **bool** | Whether product offering is enabled for the last-mile provider. | [optional] 
**poq_enabled** | **bool** | Whether product qualification is enabled for the last-mile provider. | [optional] 
**quote_enabled** | **bool** | Whether quote generation is enabled for the last-mile provider. | [optional] 
**place_order_enabled** | **bool** | Whether place order is enabled for the last-mile provider. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_profile_last_mile_api_integration import ServiceProfileLastMileApiIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileLastMileApiIntegration from a JSON string
service_profile_last_mile_api_integration_instance = ServiceProfileLastMileApiIntegration.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileLastMileApiIntegration.to_json())

# convert the object into a dict
service_profile_last_mile_api_integration_dict = service_profile_last_mile_api_integration_instance.to_dict()
# create an instance of ServiceProfileLastMileApiIntegration from a dict
service_profile_last_mile_api_integration_from_dict = ServiceProfileLastMileApiIntegration.from_dict(service_profile_last_mile_api_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


