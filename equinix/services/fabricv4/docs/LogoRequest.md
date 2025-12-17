# LogoRequest

Equinix Fabric Logo Request Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logo** | **bytearray** | Logo image file | 
**name** | **str** | Name of the Logo | 
**description** | **str** | Description of the logo | 
**type** | **str** | Type of logo | 

## Example

```python
from equinix.services.fabricv4.models.logo_request import LogoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LogoRequest from a JSON string
logo_request_instance = LogoRequest.from_json(json)
# print the JSON string representation of the object
print(LogoRequest.to_json())

# convert the object into a dict
logo_request_dict = logo_request_instance.to_dict()
# create an instance of LogoRequest from a dict
logo_request_from_dict = LogoRequest.from_dict(logo_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


