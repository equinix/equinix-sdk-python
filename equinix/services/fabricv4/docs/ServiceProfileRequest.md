# ServiceProfileRequest

Service Profile is a software definition for a named provider service and it's network connectivity requirements. This includes the basic marketing information and one or more sets of access points (a set per each access point type) fulfilling the provider service. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | [**Project**](Project.md) |  | [optional] 
**href** | **str** | Service Profile URI response attribute | [optional] [readonly] 
**type** | [**ServiceProfileTypeEnum**](ServiceProfileTypeEnum.md) |  | 
**name** | **str** | Customer-assigned service profile name | 
**uuid** | **str** | Equinix-assigned service profile identifier | [optional] 
**description** | **str** | User-provided service description should be of maximum length 375 | 
**notifications** | [**List[SimplifiedNotification]**](SimplifiedNotification.md) | Recipients of notifications on service profile change | [optional] 
**tags** | **List[str]** |  | [optional] 
**visibility** | [**ServiceProfileVisibilityEnum**](ServiceProfileVisibilityEnum.md) |  | [optional] 
**allowed_emails** | **List[str]** |  | [optional] 
**access_point_type_configs** | [**List[ServiceProfileAccessPointType]**](ServiceProfileAccessPointType.md) |  | [optional] 
**custom_fields** | [**List[CustomField]**](CustomField.md) |  | [optional] 
**marketing_info** | [**MarketingInfo**](MarketingInfo.md) |  | [optional] 
**ports** | [**List[ServiceProfileAccessPointCOLO]**](ServiceProfileAccessPointCOLO.md) |  | [optional] 
**virtual_devices** | [**List[ServiceProfileAccessPointVD]**](ServiceProfileAccessPointVD.md) |  | [optional] 
**metros** | [**List[ServiceMetro]**](ServiceMetro.md) | Derived response attribute. | [optional] 
**environments** | [**List[ProviderEnvironment]**](ProviderEnvironment.md) | Provider environments associated with this IC_PROFILE service profile. &lt;font color&#x3D;\&quot;red\&quot;&gt; &lt;sup color&#x3D;&#39;red&#39;&gt;Beta&lt;/sup&gt;&lt;/font&gt; | [optional] 
**self_profile** | **bool** | response attribute indicates whether the profile belongs to the same organization as the api-invoker. | [optional] [readonly] 
**project_id** | **str** |  | [optional] 
**last_mile_config** | [**ServiceProfileLastMileConfig**](ServiceProfileLastMileConfig.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_profile_request import ServiceProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileRequest from a JSON string
service_profile_request_instance = ServiceProfileRequest.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileRequest.to_json())

# convert the object into a dict
service_profile_request_dict = service_profile_request_instance.to_dict()
# create an instance of ServiceProfileRequest from a dict
service_profile_request_from_dict = ServiceProfileRequest.from_dict(service_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


