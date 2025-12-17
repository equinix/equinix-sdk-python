# LogoResponse

Equinix Fabric Logo Response Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 
**type** | **str** | Type of logo | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**changelog** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.logo_response import LogoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LogoResponse from a JSON string
logo_response_instance = LogoResponse.from_json(json)
# print the JSON string representation of the object
print(LogoResponse.to_json())

# convert the object into a dict
logo_response_dict = logo_response_instance.to_dict()
# create an instance of LogoResponse from a dict
logo_response_from_dict = LogoResponse.from_dict(logo_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


