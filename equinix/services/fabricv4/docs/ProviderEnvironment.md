# ProviderEnvironment

Provider Environment associated with an IC_PROFILE service profile <font color=\"red\"> <sup color='red'>Beta</sup></font>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Provider Environment URI | [optional] [readonly] 
**uuid** | **str** | Equinix-assigned provider environment identifier | [optional] 
**type** | [**ProviderEnvironmentTypeEnum**](ProviderEnvironmentTypeEnum.md) |  | [optional] 
**name** | **str** | Provider environment name | [optional] 
**description** | **str** | Provider environment description | [optional] 
**region** | **str** | Cloud provider region identifier | [optional] 
**supported_bandwidths** | **List[int]** | Supported bandwidths in Mbps | [optional] 
**metros** | [**List[ServiceMetro]**](ServiceMetro.md) | Derived response attribute. | [optional] 
**supported_features** | **List[str]** | Supported Feature Types | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.provider_environment import ProviderEnvironment

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderEnvironment from a JSON string
provider_environment_instance = ProviderEnvironment.from_json(json)
# print the JSON string representation of the object
print(ProviderEnvironment.to_json())

# convert the object into a dict
provider_environment_dict = provider_environment_instance.to_dict()
# create an instance of ProviderEnvironment from a dict
provider_environment_from_dict = ProviderEnvironment.from_dict(provider_environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


