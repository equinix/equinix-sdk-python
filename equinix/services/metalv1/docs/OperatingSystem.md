# OperatingSystem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_date** | **date** | The date when Metal&#39;s current OS image was built and released. | [optional] 
**default_operating_system** | **bool** | Default operating system for the distro. | [optional] [readonly] 
**deprecation_date** | **date** | The date when the OS is deprecated. This is the date set by the upstream operating system maintainer. | [optional] 
**distro** | **str** |  | [optional] 
**distro_label** | **str** |  | [optional] 
**end_of_life_date** | **date** | The date when the Metal OS image no longer receives any updates and may be disabled at any time. Typically the same as the deprecation date set by the upstream OS maintainers. | [optional] 
**end_of_service_date** | **date** | Metal-set date for when the OS is nearing end of life, typically 30 days before end of life. | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**licensed** | **bool** | Indicates if the OS is licensed or not. Licensed operating systems are priced according to pricing property. | [optional] 
**lifecycle_state** | **str** | Where in the lifecycle the OS image is. Possible states are - &#x60;\&quot;testing\&quot;&#x60;, &#x60;\&quot;pre_release\&quot;&#x60;, &#x60;\&quot;active\&quot;&#x60;, &#x60;\&quot;deprecated\&quot;&#x60;, &#x60;\&quot;end_of_service\&quot;&#x60;, or &#x60;\&quot;end_of_life\&quot;&#x60;. | [optional] 
**name** | **str** |  | [optional] 
**preinstallable** | **bool** | Indicates whether servers can be preinstalled with OS image in order to shorten provision time. | [optional] 
**pricing** | **object** | This object contains price per time unit and optional multiplier value if license price depends on hardware plan or components (e.g. number of cores). | [optional] 
**provisionable_on** | **List[str]** |  | [optional] 
**release_date** | **date** | The date the upstream operating system maintainer released this version of the OS. | [optional] 
**release_notes** | **str** | The current release notes for this OS image, typically in Markdown format. | [optional] 
**slug** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from equinix.services.metalv1.models.operating_system import OperatingSystem

# TODO update the JSON string below
json = "{}"
# create an instance of OperatingSystem from a JSON string
operating_system_instance = OperatingSystem.from_json(json)
# print the JSON string representation of the object
print(OperatingSystem.to_json())

# convert the object into a dict
operating_system_dict = operating_system_instance.to_dict()
# create an instance of OperatingSystem from a dict
operating_system_form_dict = operating_system.from_dict(operating_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


