# AppDomain

App Domain object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Resource URI | [optional] [readonly] 
**type** | [**AppDomainType**](AppDomainType.md) |  | [default to AppDomainType.APP_DOMAIN]
**uuid** | **str** | Equinix-assigned access point identifier | [optional] 
**name** | **str** | Customer-provided App Domain name | 
**description** | **str** | Customer-provided App Domain description | [optional] 
**state** | [**AppDomainState**](AppDomainState.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 
**change** | [**AppDomainChange**](AppDomainChange.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_domain import AppDomain

# TODO update the JSON string below
json = "{}"
# create an instance of AppDomain from a JSON string
app_domain_instance = AppDomain.from_json(json)
# print the JSON string representation of the object
print(AppDomain.to_json())

# convert the object into a dict
app_domain_dict = app_domain_instance.to_dict()
# create an instance of AppDomain from a dict
app_domain_from_dict = AppDomain.from_dict(app_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


