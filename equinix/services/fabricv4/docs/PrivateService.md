# PrivateService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.private_service import PrivateService

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateService from a JSON string
private_service_instance = PrivateService.from_json(json)
# print the JSON string representation of the object
print(PrivateService.to_json())

# convert the object into a dict
private_service_dict = private_service_instance.to_dict()
# create an instance of PrivateService from a dict
private_service_from_dict = PrivateService.from_dict(private_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


