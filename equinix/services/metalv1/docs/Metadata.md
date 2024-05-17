# Metadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_class** | **str** |  | [optional] 
**customdata** | **Dict[str, object]** |  | [optional] 
**facility** | **str** | The facility code of the instance | [optional] 
**hostname** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**iqn** | **str** |  | [optional] 
**metro** | **str** | The metro code of the instance | [optional] 
**network** | [**MetadataNetwork**](MetadataNetwork.md) |  | [optional] 
**operating_system** | **object** |  | [optional] 
**plan** | **str** | The plan slug of the instance | [optional] 
**private_subnets** | **List[str]** | An array of the private subnets | [optional] 
**reserved** | **bool** |  | [optional] 
**specs** | **object** | The specs of the plan version of the instance | [optional] 
**ssh_keys** | **List[str]** |  | [optional] 
**state** | **str** | The current state the instance is in.  * When an instance is initially created it will be in the &#x60;queued&#x60; state until it is picked up by the provisioner. * Once provisioning has begun on the instance it&#39;s state will move to &#x60;provisioning&#x60;. * When an instance is deleted, it will move to &#x60;deprovisioning&#x60; state until the deprovision is completed and the instance state moves to &#x60;deleted&#x60;. * If an instance fails to provision or deprovision it will move to &#x60;failed&#x60; state. * Once an instance has completed provisioning it will move to &#x60;active&#x60; state. * If an instance is currently powering off or powering on it will move to &#x60;powering_off&#x60; or &#x60;powering_on&#x60; states respectively.  * When the instance is powered off completely it will move to the &#x60;inactive&#x60; state. * When an instance is powered on completely it will move to the &#x60;active&#x60; state. * Using the reinstall action to install a new OS on the instance will cause the instance state to change to &#x60;reinstalling&#x60;. * When the reinstall action is complete the instance will move to &#x60;active&#x60; state. | [optional] 
**switch_short_id** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**volumes** | **List[str]** |  | [optional] 

## Example

```python
from equinix_metal.models.metadata import Metadata

# TODO update the JSON string below
json = "{}"
# create an instance of Metadata from a JSON string
metadata_instance = Metadata.from_json(json)
# print the JSON string representation of the object
print(Metadata.to_json())

# convert the object into a dict
metadata_dict = metadata_instance.to_dict()
# create an instance of Metadata from a dict
metadata_form_dict = metadata.from_dict(metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


