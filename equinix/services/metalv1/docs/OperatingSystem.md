# OperatingSystem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_date** | **date** | The date on which the current OS image was build and released | [optional] 
**default_operating_system** | **bool** | Default operating system for the distro. | [optional] [readonly] 
**deprecation_date** | **date** | The date when the OS is deprecated | [optional] 
**distro** | **str** |  | [optional] 
**distro_label** | **str** |  | [optional] 
**end_of_life_date** | **date** | The OS no longer receives any updates and may be disabled at any time | [optional] 
**end_of_service_date** | **date** | When the OS is nearing end of life, typically 30 days before end of life | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**licensed** | **bool** | Licenced OS is priced according to pricing property | [optional] 
**lifecycle_state** | **str** | Where in the support lifecycle the OS is | [optional] 
**name** | **str** |  | [optional] 
**preinstallable** | **bool** | Servers can be already preinstalled with OS in order to shorten provision time. | [optional] 
**pricing** | **object** | This object contains price per time unit and optional multiplier value if licence price depends on hardware plan or components (e.g. number of cores) | [optional] 
**provisionable_on** | **List[str]** |  | [optional] 
**release_date** | **date** | The date when the OS was released | [optional] 
**release_notes** | **str** | The current release notes for this OS image, typically in Markdown format | [optional] 
**slug** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.operating_system import OperatingSystem

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


