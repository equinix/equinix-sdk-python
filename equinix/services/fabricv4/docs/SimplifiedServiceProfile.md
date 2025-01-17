# SimplifiedServiceProfile

Service Profile is a software definition for a named provider service and it's network connectivity requirements. This includes the basic marketing information and one or more sets of access points (a set per each access point type) fulfilling the provider service. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Service Profile URI response attribute | [optional] [readonly] 
**type** | [**ServiceProfileTypeEnum**](ServiceProfileTypeEnum.md) |  | [optional] 
**name** | **str** | Customer-assigned service profile name | [optional] 
**uuid** | **str** | Equinix-assigned service profile identifier | [optional] 
**description** | **str** | User-provided service description should be of maximum length 375 | [optional] 
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
**self_profile** | **bool** | response attribute indicates whether the profile belongs to the same organization as the api-invoker. | [optional] 
**project_id** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.simplified_service_profile import SimplifiedServiceProfile

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedServiceProfile from a JSON string
simplified_service_profile_instance = SimplifiedServiceProfile.from_json(json)
# print the JSON string representation of the object
print(SimplifiedServiceProfile.to_json())

# convert the object into a dict
simplified_service_profile_dict = simplified_service_profile_instance.to_dict()
# create an instance of SimplifiedServiceProfile from a dict
simplified_service_profile_from_dict = SimplifiedServiceProfile.from_dict(simplified_service_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


