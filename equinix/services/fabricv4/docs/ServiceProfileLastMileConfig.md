# ServiceProfileLastMileConfig

Last-mile configuration for the service profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_integration** | [**ServiceProfileLastMileApiIntegration**](ServiceProfileLastMileApiIntegration.md) |  | [optional] 
**product_catalogs** | [**List[ServiceProfileLastMileProductCatalog]**](ServiceProfileLastMileProductCatalog.md) | Last-mile provider catalogs. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_profile_last_mile_config import ServiceProfileLastMileConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileLastMileConfig from a JSON string
service_profile_last_mile_config_instance = ServiceProfileLastMileConfig.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileLastMileConfig.to_json())

# convert the object into a dict
service_profile_last_mile_config_dict = service_profile_last_mile_config_instance.to_dict()
# create an instance of ServiceProfileLastMileConfig from a dict
service_profile_last_mile_config_from_dict = ServiceProfileLastMileConfig.from_dict(service_profile_last_mile_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


